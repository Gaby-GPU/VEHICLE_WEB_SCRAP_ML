from setuptools import setup, find_packages

setup(
    name='Vehicle_Web_Scraping_Project',
    version='0.1.0',  
    description='Vehicle web scraping project for data analysis',
    author='Gabriel Páris Uzzo',
    author_email='uzzogabriel77@gmail.com',
    url='https://github.com/Gaby-GPU/VEHICLE_WEB_SCRAP_ML.git',  
    packages=find_packages(),  
    install_requires=[
        'requests',
        'beautifulsoup4',
        'pandas',
    ],
    entry_points={
        'console_scripts': [
            'project_wb_ml=core.main:main',  
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: Apache License 2.0',  
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',  
)