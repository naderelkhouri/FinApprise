import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from django.core.management import call_command
from django.contrib.auth.models import User
from apps.revenues.models import RecipeCategoriesRevenues, RecipeSubcategoriesRevenues

def initialize():
    print("🔄 Verificando e aplicando migrações...")
    call_command('migrate', interactive=False)
    
    # Criar superusuário padrão se nenhum usuário existir
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser('admin', 'admin@finapprise.local', 'admin123')
        admin.first_name = 'Administrador'
        admin.last_name = 'FinApprise'
        admin.save()
        print("✅ Usuário padrão criado com sucesso: admin / admin123")
    else:
        print("ℹ️ Usuário admin já existente.")
        
    # Inicializar categorias e subcategorias contábeis se vazias
    admin_user = User.objects.filter(username='admin').first()
    if admin_user and not RecipeCategoriesRevenues.objects.exists():
        cat_oper, _ = RecipeCategoriesRevenues.objects.get_or_create(
            category_name='Receitas Operacionais',
            defaults={'autor': admin_user}
        )
        cat_finan, _ = RecipeCategoriesRevenues.objects.get_or_create(
            category_name='Receitas Financeiras',
            defaults={'autor': admin_user}
        )
        cat_outras, _ = RecipeCategoriesRevenues.objects.get_or_create(
            category_name='Outras Receitas',
            defaults={'autor': admin_user}
        )
        
        RecipeSubcategoriesRevenues.objects.get_or_create(
            category_name=cat_oper,
            subcategory_name='Venda de Mercadorias',
            defaults={'autor': admin_user}
        )
        RecipeSubcategoriesRevenues.objects.get_or_create(
            category_name=cat_oper,
            subcategory_name='Prestação de Serviços',
            defaults={'autor': admin_user}
        )
        RecipeSubcategoriesRevenues.objects.get_or_create(
            category_name=cat_finan,
            subcategory_name='Rendimentos de Aplicação',
            defaults={'autor': admin_user}
        )
        RecipeSubcategoriesRevenues.objects.get_or_create(
            category_name=cat_finan,
            subcategory_name='Descontos Obtidos',
            defaults={'autor': admin_user}
        )
        print("✅ Categorias e subcategorias contábeis iniciais configuradas!")

if __name__ == '__main__':
    initialize()
