#!/usr/bin/env python3
"""
FinApprise - Desktop Application Launcher (Linux GTK3 + WebKit2)
Fornece uma experiência nativa de desktop com janela dedicada, ícone e ciclo de vida isolado.
"""

import sys
import os
import time
import socket
import signal
import subprocess
import threading
import urllib.request
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(BASE_DIR))
sys.path.insert(0, str(BASE_DIR / 'apps'))

ICON_PATH = str(BASE_DIR / 'assets' / 'icon-256.png')
if not os.path.exists(ICON_PATH):
    ICON_PATH = str(BASE_DIR / 'assets' / 'icon.png')

def find_free_port(start_port=8000):
    for port in range(start_port, start_port + 100):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            if s.connect_ex(('127.0.0.1', port)) != 0:
                return port
    return 8000

def wait_for_server(url, timeout=10):
    start = time.time()
    while time.time() - start < timeout:
        try:
            with urllib.request.urlopen(url, timeout=1) as response:
                if response.status in (200, 302):
                    return True
        except Exception:
            time.sleep(0.2)
    return False

class FinAppriseDesktop:
    def __init__(self):
        self.port = find_free_port()
        self.url = f"http://127.0.0.1:{self.port}"
        self.server_process = None

    def start_server(self):
        # Inicializa banco de dados e dados padrão
        try:
            from init_db import initialize
            initialize()
        except Exception as e:
            print(f"[FinApprise] Erro na inicialização do banco: {e}")

        python_bin = str(BASE_DIR / '.venv' / 'bin' / 'python')
        if not os.path.exists(python_bin):
            python_bin = sys.executable

        env = os.environ.copy()
        env['PYTHONUNBUFFERED'] = '1'

        print(f"🚀 Iniciando servidor FinApprise em {self.url}...")
        self.server_process = subprocess.Popen(
            [python_bin, str(BASE_DIR / 'manage.py'), 'runserver', f'127.0.0.1:{self.port}', '--noreload'],
            cwd=str(BASE_DIR),
            env=env,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if not wait_for_server(f"{self.url}/login/", timeout=12):
            print("⚠️ Servidor demorou a responder, prosseguindo com abertura da janela...")
        else:
            print("✅ Servidor FinApprise pronto!")

    def stop_server(self):
        if self.server_process:
            print("🛑 Encerrando servidor FinApprise...")
            try:
                self.server_process.terminate()
                self.server_process.wait(timeout=3)
            except Exception:
                self.server_process.kill()
            self.server_process = None

    def run_gtk(self):
        import gi
        gi.require_version('Gtk', '3.0')
        gi.require_version('WebKit2', '4.1')
        from gi.repository import Gtk, WebKit2, GLib, GdkPixbuf, Gdk

        GLib.set_prgname("finapprise")
        GLib.set_application_name("FinApprise")

        window = Gtk.Window(title="FinApprise - Contabilidade & Gestão Financeira")
        window.set_default_size(1320, 860)
        window.set_position(Gtk.WindowPosition.CENTER)

        # Configurar Ícone
        if os.path.exists(ICON_PATH):
            try:
                pixbuf = GdkPixbuf.Pixbuf.new_from_file(ICON_PATH)
                window.set_icon(pixbuf)
                Gtk.Window.set_default_icon(pixbuf)
            except Exception as e:
                print(f"[FinApprise] Não foi possível carregar ícone: {e}")

        # Configurar WebView WebKit2
        webview = WebKit2.WebView()
        settings = webview.get_settings()
        settings.set_enable_javascript(True)
        settings.set_enable_developer_extras(False)
        settings.set_enable_page_cache(True)
        settings.set_enable_smooth_scrolling(True)

        scrolled = Gtk.ScrolledWindow()
        scrolled.add(webview)
        window.add(scrolled)

        # Atalhos de Teclado
        def on_key_press(widget, event):
            state = event.state & Gtk.accelerator_get_default_mod_mask()
            keyval = event.keyval

            # F11: Tela Cheia
            if keyval == Gdk.KEY_F11:
                if window.is_fullscreen:
                    window.unfullscreen()
                    window.is_fullscreen = False
                else:
                    window.fullscreen()
                    window.is_fullscreen = True
                return True

            # F5 ou Ctrl+R: Recarregar
            if keyval == Gdk.KEY_F5 or (state == Gdk.ModifierType.CONTROL_MASK and keyval in (Gdk.KEY_r, Gdk.KEY_R)):
                webview.reload()
                return True

            # Ctrl + : Zoom In
            if state == Gdk.ModifierType.CONTROL_MASK and keyval in (Gdk.KEY_plus, Gdk.KEY_equal, Gdk.KEY_KP_Add):
                webview.set_zoom_level(webview.get_zoom_level() + 0.1)
                return True

            # Ctrl - : Zoom Out
            if state == Gdk.ModifierType.CONTROL_MASK and keyval in (Gdk.KEY_minus, Gdk.KEY_underscore, Gdk.KEY_KP_Subtract):
                webview.set_zoom_level(max(0.5, webview.get_zoom_level() - 0.1))
                return True

            # Ctrl 0 : Reset Zoom
            if state == Gdk.ModifierType.CONTROL_MASK and keyval in (Gdk.KEY_0, Gdk.KEY_KP_0):
                webview.set_zoom_level(1.0)
                return True

            return False

        window.is_fullscreen = False
        window.connect("key-press-event", on_key_press)

        # Fechamento Limpo
        def on_destroy(widget):
            self.stop_server()
            Gtk.main_quit()

        window.connect("destroy", on_destroy)

        # Carregar URL
        webview.load_uri(self.url)
        window.show_all()
        Gtk.main()

    def run(self):
        self.start_server()
        has_display = bool(os.environ.get('DISPLAY') or os.environ.get('WAYLAND_DISPLAY'))
        
        if has_display:
            try:
                self.run_gtk()
                return
            except Exception as e:
                print(f"[FinApprise] Falha na interface GTK3 ({e}). Abrindo no navegador...")

        # Fallback para navegador padrão se sem GTK/display
        import webbrowser
        print(f"🌐 Abrindo FinApprise no navegador em {self.url}...")
        webbrowser.open(self.url)

        try:
            print("Pressione Ctrl+C para encerrar o FinApprise.")
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            pass
        finally:
            self.stop_server()

def main():
    app = FinAppriseDesktop()

    def sig_handler(sig, frame):
        app.stop_server()
        sys.exit(0)

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    app.run()

if __name__ == '__main__':
    main()
