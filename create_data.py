import os
import glob
import pandas as pd

df = pd.DataFrame(columns= ['id', 'tonometer(mV)', 'categorical_id', 'gender', 'age', 'BMI', 'hypertension', 'fregnant'])

folder_path = 'D:\Research Milestones\A Dataset of Synchronized Signals from Wearable Cardiovascular Monitoring Sensors'
data_list = []
id_list = []
gender_list = []
age_list  = []
BMI_list = []
hypertension_list = []
fregnant_list = []
overallData = pd.read_excel(os.path.join(folder_path,'Participant_Health_Data.xlsx'), sheet_name='Sheet1')
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        id = os.path.splitext(filename)[0]
        # overallData = pd.read_excel(os.path.join(folder_path,'Participant_Health_Data.xlsx'), sheet_name='Sheet1')
        print(overallData.loc[overallData['Participant Identifier'] == id]['Gender'].reset_index(drop=True).values.tolist()[0])
        gen = overallData.loc[overallData['Participant Identifier'] == id]['Gender'].reset_index(drop=True).values.tolist()[0]
        age = overallData.loc[overallData['Participant Identifier'] == id]['Age'].reset_index(drop=True).values.tolist()[0]
        BMI = overallData.loc[overallData['Participant Identifier'] == id]['BMI'].reset_index(drop=True).values.tolist()[0]
        hypertension = overallData.loc[overallData['Participant Identifier'] == id]['Medicated for Hypertension?'].reset_index(drop=True).values.tolist()[0]
        fregnant = overallData.loc[overallData['Participant Identifier'] == id]['Pregnant?'].reset_index(drop=True).values.tolist()[0]
        column_values = pd.read_csv(os.path.join(folder_path, filename))['Tonometer (mV)']
        print(column_values)
        for d in column_values.values.tolist():
            data_list.append(d)
            id_list.append(id)         
            gender_list.append(gen)
            age_list.append(age)
            BMI_list.append(BMI)
            hypertension_list.append(hypertension)
            fregnant_list.append(fregnant)
print(len(id_list))
print(id_list[1:3])
print(data_list[:10])
df['tonometer(mV)'] = pd.concat([df['tonometer(mV)'], pd.Series(data_list)], ignore_index=True)
df['id'] = pd.concat([df['id'], pd.Series(id_list)], ignore_index= True)      
df['categorical_id'] = pd.concat([df['categorical_id'], pd.Series(id_list)], ignore_index= True)
df['gender'] = pd.concat([df['gender'], pd.Series(gender_list)], ignore_index= True)
df['age'] = pd.concat([df['age'], pd.Series(age_list)], ignore_index= True)
df['BMI'] = pd.concat([df['BMI'], pd.Series(BMI_list)], ignore_index= True)
df['hypertension'] = pd.concat([df['hypertension'], pd.Series(hypertension_list)], ignore_index= True)
df['fregnant'] = pd.concat([df['fregnant'], pd.Series(fregnant_list)], ignore_index= True)
  
        # df['tonometer(mV)'].append(column_values, ignore_index=True)
        # for data in range(len(column_values)):
        #     df['id'].append(pd.Series(id))
        #     df['tonometer(mV)'].append(pd.Series(column_values[data]))

print(df)

