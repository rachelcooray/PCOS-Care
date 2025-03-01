# PCOS Care: A Web Application for Diagnosing PCOS Using Machine Learning

## **Overview**  
PCOS Care is a web-based application that predicts the likelihood of Polycystic Ovary Syndrome (PCOS) using machine learning. The platform allows users to input their health data, receive a risk assessment, and access educational resources about PCOS.  

## **Features**  
1. User-friendly interface for entering health data  
2. Machine learning-based PCOS risk prediction   
3. Visualization of results  
4. Educational content on PCOS symptoms, causes, and management  

## **Tech Stack Used**  
- **Frontend:** Streamlit  
- **Machine Learning:** scikit-learn (Random Forest/SVM)  
- **Data Processing:** Pandas, NumPy  
- **Visualization:** Matplotlib, Seaborn  

## **Installation**  

Follow these steps to install and run the project:  

### **1. Download and Extract the Project**  
- Download the ZIP file containing the project.  
- Extract the contents to a suitable directory on your system.  

### **2. Navigate to the Frontend Folder**  
- Open a terminal or command prompt.  
- Change the directory to the frontend folder using the following command:  
  ```bash
  cd PCOS-Care/frontend
  ```

### **3. Run the Streamlit Application**  
- Start the application by running:  
  ```bash
  streamlit run main.py
  ```
- This will launch the web application in your default browser.  

### **4. Stop the Application**  
- To stop the application, type `CTRL + C` in the terminal.

## **Usage**  
1. Open the web application in your browser.  
2. Enter your health data (e.g., symptoms, medical history).  
3. Click **Submit** to get a predicted PCOS risk assessment.  
4. View results and access educational resources.  


## **To-Do List**  
- [ ] Improve appearance of the frontend
- [ ] Improve result visualization
- [ ] Improve information page
- [v] Link frontend and backend
- [v] Hosting

