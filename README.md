# Fleet Service to Vendor Bill Automation

![Odoo Version](https://img.shields.io/badge/Odoo-19.0-purple.svg) 
![License](https://img.shields.io/badge/License-LGPL--3-blue.svg)

This Odoo module streamlines the workflow between **Fleet Management** and **Accounting** by automating the creation of vendor bills directly from completed service logs.

## 🚀 Key Features

* **✅ Automatic Bill Creation**: Automatically generates a Vendor Bill (`account.move`) when a Fleet Service log is moved to the 'Done' state.
* **🔗 Reference Linking**: Establishes a direct link between the generated Vendor Bill and the Fleet Service log for seamless tracking.
* **📱 Smart Navigation**: Adds a smart button to the Fleet Service form to jump directly to the related Vendor Bill.
* **📝 Dynamic Descriptions**: Automatically populates bill line descriptions using service type and vehicle information.
* **⚠️ Vendor Validation**: Prevents errors by ensuring a vendor is assigned before attempting to create a bill.

## 🛠 Installation

1.  Clone this repository into your Odoo `addons` folder.
2.  Update your Odoo configuration to include the new path.
3.  Go to **Apps** -> **Update Apps List**.
4.  Search for `Fleet Service Invoicing` and click **Install**.

## ⚙️ How it Works

1.  Navigate to **Fleet** -> **Services**.
2.  Select a service log and ensure a **Vendor** is selected.
3.  Set the service status to **Done**.
4.  A **Vendor Bill** will be created automatically in the **Accounting/Invoicing** module.
5.  Use the smart button on the top right of the service form to view the bill.

## 🗺️ Roadmap (Upcoming Features)

- [ ] **Automatic Analytic Account Mapping**: Automatically assign the vehicle's analytic account to the bill lines for better cost tracking.
- [ ] **Multi-currency Support**: Enhanced support for international fleet operations.
- [ ] **Configuration Toggle**: Enable/Disable automatic creation per service type.

## 📄 License
This module is licensed under the **LGPL-3** license.

---
*Developed with ❤️ for the Odoo Community.*
