# Parashoot ERP

Parashoot ERP is a project developed using Python Django framework. It aims to provide a comprehensive ERP solution with modules including Location Setup, Customer Management, Companies Management, Inventory Management, Accounting, Marketing, Employee Management, and Reports. Please note that this project is still a work in progress.

## Modules

- **Location Setup**: 
  - Description: Module for setting up various locations.
- **Customer Management**: 
  - Description: Module for managing customer data.
- **Companies Management**: 
  - Description: Module for managing company data.
- **Inventory Management**: 
  - Description: Module for managing inventory.
- **Accounting**: 
  - Description: Module for accounting purposes.
- **Marketing**: 
  - Description: Module for marketing activities.
- **Employee Management**: 
  - Description: Module for managing employee data.
- **Reports**: 
  - Description: Module for generating reports.

## Installation

To install and run this Django application, follow these steps:

1. Clone the repository:

git clone https://github.com/daniyalcomsoft/ParashootERP.git
cd ParashootERP


2. Install Python (if not already installed). You can download it from the [official Python website](https://www.python.org/downloads/).

3. Install Django and other dependencies:

    pip install -r requirements.txt


4. Set up your database configuration in `settings.py`. By default, the project uses SQLite, but you can also configure it to use PostgreSQL.

5. Apply migrations:

    python manage.py migrate


6. Run the development server:

    python manage.py runserver


7. Access the application in your web browser at `http://localhost:8000`.

## Technologies Used

- Python
- Django
- HTML
- CSS
- JavaScript
- PostgreSQL
- SQLite

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these guidelines:
- Fork the repository
- Create your feature branch (`git checkout -b feature/YourFeature`)
- Commit your changes (`git commit -m 'Add some feature'`)
- Push to the branch (`git push origin feature/YourFeature`)
- Create a new Pull Request

## License

This project is licensed under the [MIT License](LICENSE).
