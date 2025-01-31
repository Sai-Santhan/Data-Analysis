# Data-Analysis (Sales Report Generator)

A secure, scalable, responsive, mobile-first, maintainable, reliable, cloud-first, containerized, with CI/CD automation
implemented Data Analysis application.

**Get insights about your product sales by generating report PDFs with 3 different chart choices - (Bar, Line and Pie
charts) and 2 result choices - (By Transaction and Sales Date) from the sales list, which is loaded by uploading a
particularly formatted CSV file(shown below).**

![python](http://ForTheBadge.com/images/badges/made-with-python.svg)
![Python-3.10.1](https://img.shields.io/badge/Python-3.10.1-blue.svg?style=for-the-badge&logo=python&logoColor=ffdd54)
<a href="http://www.djangoproject.com/"><img src="https://www.djangoproject.com/m/img/badges/djangopowered126x54.gif" border="0" alt="Powered by Django." title="Powered by Django." /></a>

## Features

- Secure Argon2 password hashing
- HTTPS enabled everywhere with valid TLS certificate
- Data visualization with NumPy, Pandas, Matplotlib, Seaborn
- Responsive and visually appealing UI with Bootstrap
- Generate reports and view or download them in PDF format
- 3 different chart choices - Bar, Line and Pie
- 2 result choices - Transaction and Sales Date
- Drag and Drop CSV file upload using Dropzone.js
- Jinja templating engine with inheritance for DRY code
- Containerized with Docker
- Scalable Kubernetes Deployment using DigitalOcean Managed Kubernetes
- Load balanced using kubernetes service in DigitalOcean
- DigitalOcean Cloud-native Deployment
- Database storage with DigitalOcean managed PostgreSQL database
- DigitalOcean Spaces for storage of uploaded CSV files and static files
- Automated Security Scanning with Snyk
- CI/CD with GitHub Actions

## Tech Stack

<div style="display: flex; align-items: flex-start;"><img src="https://techstack-generator.vercel.app/python-icon.svg" alt="icon" width="56" height="56" /><img src="https://techstack-generator.vercel.app/django-icon.svg" alt="icon" width="56" height="56" /><img src="https://techstack-generator.vercel.app/js-icon.svg" alt="icon" width="56" height="56" /><img src="https://techstack-generator.vercel.app/docker-icon.svg" alt="icon" width="56" height="56" /><img src="https://techstack-generator.vercel.app/kubernetes-icon.svg" alt="icon" width="56" height="56" /><img src="https://techstack-generator.vercel.app/restapi-icon.svg" alt="icon" width="56" height="56" /></div>

<a href="https://github.com/Sai-Santhan/Data-Analysis/actions"><img height="90" src="https://skillicons.dev/icons?i=githubactions" alt="Github Actions" title="Github Actions"/></a>

![Jinja](https://www.vectorlogo.zone/logos/pocoo_jinja/pocoo_jinja-icon.svg)
<img height="55" src="https://user-images.githubusercontent.com/25181517/183898054-b3d693d4-dafb-4808-a509-bab54cf5de34.png" alt="Bootstrap" title="Bootstrap" />
<img height="53" src="https://raw.githubusercontent.com/wappalyzer/wappalyzer/master/src/drivers/webextension/images/icons/Dropzone.svg" alt="Dropzone" title="Dropzone"/>
![Gunicorn](https://www.vectorlogo.zone/logos/gunicorn/gunicorn-icon.svg)
<img height="60" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/digitalocean/digitalocean-original.svg" alt="Digital Ocean" title="Digital Ocean"/>
![PostgreSQL](https://skillicons.dev/icons?i=postgresql)
<img height="55" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/numpy/numpy-original.svg" alt="Numpy" title="Numpy"/>
<img height="55" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" />
<img height="55" src="https://matplotlib.org/_static/images/documentation.svg" />
<img height="55" src="https://raw.githubusercontent.com/gilbarbara/logos/9c6e5e9ef3c297da414a4809ae9f0f56a6384e91/logos/seaborn-icon.svg" />
<img height="55" src="https://snyk.io/wp-content/uploads/patch-alert.svg" alt="">

### *Other libraries: Argon2, pillow, Smart-Open, xhtml2pdf, Boto3, django-crispy-forms*

## Usage with Screenshots

> ### 1. CSV Format for uploading

![CSV Format](src/static/screenshots/meme-csv.png?raw=true "CSV Format")

> #### ***For Experimenting - Download [CSV](src/static/meme.csv "CSV file in src/static folder")***

| Pos | Transaction id | Product    | Quantity | Customer | Date       |
|-----|----------------|------------|----------|----------|------------|
| 1   | E201           | TV         | 1        | Suresh   | 2022-10-18 |
| 2   | E202           | Smartwatch | 3        | Ramesh   | 2022-10-18 |
| 3   | E203           | TV         | 1        | Baburao  | 2022-10-20 |
| 4   | E304           | iphone     | 2        | Suresh   | 2022-10-21 |
| 5   | E305           | Laptop     | 2        | Binod    | 2022-10-23 |
| 6   | E320           | iphone     | 5        | Binod    | 2022-10-23 |
| 7   | E412           | Laptop     | 2        | Suresh   | 2022-10-23 |
| 8   | E445           | Smartwatch | 4        | Ramesh   | 2022-10-24 |
 

> ### 2. After Login, go to 'Upload CSV' and upload the above File

![Upload](src/static/screenshots/upload.png?raw=true "Upload")

> ### 3. View list of product sales(extracted from CSV) by going to 'Sales-List'

![Sales List](src/static/screenshots/sales.png?raw=true "Sales List")

> ### 4. Go to 'Home' to Analyze the sales data using sales date or transaction

![Home](src/static/screenshots/home.png?raw=true "Home")

> ### 5. View the Chart at bottom of 'Home' page and Add Report

![Chart](src/static/screenshots/chart.png?raw=true "Chart")

> ### 6. Go to 'Reports' to view reports (detail view or PDF view)

![Report](src/static/screenshots/report.png?raw=true "Report")

> ### 7. Report PDF (option to download)

![PDF](src/static/screenshots/pdf.png?raw=true "PDF")
