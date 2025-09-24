# 🚗 Health → Vehicle Insurance Prediction

**Predict whether health insurance customers will be interested in purchasing vehicle insurance.**

---

## 📌 Problem Context
Our client is an **Insurance Company** that provides Health Insurance. They now want to predict whether existing policyholders will also be interested in purchasing **Vehicle Insurance**.  

Why is this important?  
- Helps optimize **communication strategy**.  
- Improves **customer targeting**.  
- Increases **revenue** via cross-selling.  

---

## 📊 Dataset Description

We are provided with **train** and **test** datasets containing demographic, vehicle, and policy-related details of customers.  

### Train Data  
| Variable              | Definition |
|------------------------|------------|
| `id`                  | Unique ID for the customer |
| `Gender`              | Gender of the customer |
| `Age`                 | Age of the customer |
| `Driving_License`     | 0 = No Driving License, 1 = Has Driving License |
| `Region_Code`         | Region code of the customer |
| `Previously_Insured`  | 1 = Already has Vehicle Insurance, 0 = Does not have Vehicle Insurance |
| `Vehicle_Age`         | Age of the Vehicle |
| `Vehicle_Damage`      | 1 = Previously damaged, 0 = Not damaged |
| `Annual_Premium`      | Premium amount per year |
| `Policy_Sales_Channel`| Outreach channel code (Agent, Phone, Email, etc.) |
| `Vintage`             | Number of days associated with the company |
| `Response`            | Target → 1 = Interested in Vehicle Insurance, 0 = Not Interested |

### Test Data  
Same as train, but **without** the `Response` column.  

### Submission Format  
| Variable         | Definition |
|------------------|------------|
| `id`             | Customer ID |
| `Response`       | Predicted class (1 = Interested, 0 = Not Interested) |
| `Response_Prob`  | Probability of being interested |

---

## ⚙️ Evaluation Metric
The competition is evaluated using **ROC AUC Score**.  

- **Public Leaderboard**: 40% of test data.  
- **Private Leaderboard**: Remaining 60% of test data.  

---

## 🧰 Requirements
Install dependencies with:

```bash
pip install -r requirements.txt
