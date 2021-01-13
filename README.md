Orteal-PyBilling

A simple billing app under development. Open source. 

What works: Invoice, item, company, tax slabs creation and modification. Invoice printing.
Note 1: Exception handling not fully implemented yet. GTK auto handling is good enough to avoid crashes. 

Target OS: Ubuntu 20.04
Dependencies: pickledb, appdirs, fpdf, GTK3, Python3
Implementions: GTK3 GUI Library, python for coding, pickleDB database 

Packaged release: https://github.com/BT40/OrtealPyBilling/releases/tag/0.1
(Contains pip dependencies pickledb, appdirs, fpdf. No need to install these separately)

How to run zipapp (packaged version): 
1. Before running this app, make sure your system has GTK-3 and Python3 installed. Ubuntu 20.04 and above come preloaded with these dependencies, so nothing special needs to be done.
2. Download the packaged file from above provided link or releases section of this repository.
3. Move to the directory where package is downloaded and open terminal (right click on black space in file manager and select Open Terminal.)
4. Type below command:
    python3 src.pyz 

Running app from source code:
1. Download source code
2. Install dependencies
3. Move to src folder (in terminal)
4. Run by typing below command:
    python3 ortealbilling.py

Project started on 16 june 2020
Original author: BT40


Instructions/Short manual
1. First time running this app, please create your company details by clicking on "More", then "Manage", and finally clicking on Your company details
2. Data storage directory (ortealbilling_data) will be created in user's home folder. In this directory, invoices folder will contain pdf invoices. Other folders are used for internal databases which store app data. Layman user should only interact with invoices folder.
 

