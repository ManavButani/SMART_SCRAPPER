# Smart Scrapper API Documentation

## Server Information
**Base URL:** [https://smart-scrapper.onrender.com/docs](https://smart-scrapper.onrender.com/docs)

## Available Endpoints
For a comprehensive list of all available endpoints, refer to the documentation provided here: [Endpoints Documentation](https://drive.google.com/file/d/1963BrT_oCFwIi2L-CA9bBw_HR3MaPX4X/view?usp=drive_link)

---

## Step 1: Register Yourself
**Endpoint:** `/scrapper_application/user/register/`

### Input
Download the input format from the following link:
[Register Input JSON](https://drive.google.com/file/d/1QS7XFJo40WBgrAU2wRFWE_F31sOJAZVq/view?usp=drive_link)

---

## Step 2: Authorize Yourself
**Endpoint:** `/scrapper_application/auth/login/`

### Input
Download the input format from the following link:
[Authorization Input JSON](https://drive.google.com/file/d/1rsTnRkledle8l69qO-nOud9eYOsCcr6_/view?usp=drive_link)

### Note
You are authorized for **30 minutes** only. After this period, you need to reauthorize yourself.

---

## Step 3: Scrap Home Page
**Endpoint:** `/scrapper_application/scrap/home_page/`

### Input
Download the input format from the following link:
[Home Page Scraping Input JSON](https://drive.google.com/file/d/1bjeMqxhzbatInbY3PDQ6fx1XH85VYlPX/view?usp=drive_link)

### Output
The output can be downloaded from the following link:
[Home Page Scraping Output JSON](https://drive.google.com/file/d/1QrOInWLzTxdAQjklyyb7l-q10qrh_vXG/view?usp=drive_link)

### Note
For invalid cases such as:
- **Invalid URL**
- **Invalid `openai_key`**
- **Invalid Model**

Appropriate error responses are provided.

---

