#Nota: Casi todo en esta aplicacion permanecera igual, lo unico que cambia es los contenidos de inputdata
class Modelo:
    

#Aqui se ponen los valores que se reciben del cuestionario del frontend
#inputdata = {'Music':5, 'Music1':'Slow Song', 'Music2':'Punk', 'Music3':'Rock n roll', 'Movies':5, 'Movies1':'Horror', 'Movies2':'War',
 #'Subject':'Geography', 'Pastime':'Art exhibitions', 'Fear':'Fear of public speaking', 'Smoking':'current smoker', 'Alcohol':'drink a lot',
 #'Phrases1':'Daily events', 'Phrases2':'Loss of interest', 'Phrases3':'Borrowed stuff', 'Phrases4':'Cheating in school', 'Punctuality':'i am often early',
 #'Lying':'everytime it suits me', 'Important1':'Responding to a serious letter', 'Important2':'Assertiveness', 'Important3':'Interests or hobbies',
 #'Internet usage':'few hours a day'}
    def predict(inputdata):
        import pandas as pd
        from sklearn.ensemble import RandomForestClassifier
        from sklearn import tree
        from sklearn import preprocessing
        import pickle
        random_forest = pickle.load(open('./random_forest.sav', 'rb'))
        out_df = pickle.load(open('./outputlabels.sav', 'rb'))
        in_df = pickle.load(open('./inputlabels.sav', 'rb'))

        label_encoder = preprocessing.LabelEncoder()
        
        label_encoder.fit(in_df["Music1"].astype(str))
        inputdata["Music1"]=label_encoder.transform([inputdata["Music1"]])[0]
        
        label_encoder.fit(in_df["Music2"].astype(str))
        inputdata["Music2"]=label_encoder.transform([inputdata["Music2"]])[0]
        
        label_encoder.fit(in_df["Music3"].astype(str))
        inputdata["Music3"]=label_encoder.transform([inputdata["Music3"]])[0]
        
        label_encoder.fit(in_df["Movies1"].astype(str))
        inputdata["Movies1"]=label_encoder.transform([inputdata["Movies1"]])[0]
        
        label_encoder.fit(in_df["Movies2"].astype(str))
        inputdata["Movies2"]=label_encoder.transform([inputdata["Movies2"]])[0]
        
        label_encoder.fit(in_df["Subject"].astype(str))
        inputdata["Subject"]=label_encoder.transform([inputdata["Subject"]])[0]
        
        label_encoder.fit(in_df["Pastime"].astype(str))
        inputdata["Pastime"]=label_encoder.transform([inputdata["Pastime"]])[0]
        
        label_encoder.fit(in_df["Fear"].astype(str))
        inputdata["Fear"]=label_encoder.transform([inputdata["Fear"]])[0]
        
        label_encoder.fit(in_df["Smoking"].astype(str))
        inputdata["Smoking"]=label_encoder.transform([inputdata["Smoking"]])[0]
        
        label_encoder.fit(in_df["Alcohol"].astype(str))
        inputdata["Alcohol"]=label_encoder.transform([inputdata["Alcohol"]])[0]
        
        label_encoder.fit(in_df["Phrases1"].astype(str))
        inputdata["Phrases1"]=label_encoder.transform([inputdata["Phrases1"]])[0]
        
        label_encoder.fit(in_df["Phrases2"].astype(str))
        inputdata["Phrases2"]=label_encoder.transform([inputdata["Phrases2"]])[0]
        
        label_encoder.fit(in_df["Phrases3"].astype(str))
        inputdata["Phrases3"]=label_encoder.transform([inputdata["Phrases3"]])[0]
        
        label_encoder.fit(in_df["Phrases4"].astype(str))
        inputdata["Phrases4"]=label_encoder.transform([inputdata["Phrases4"]])[0]
        
        label_encoder.fit(in_df["Punctuality"].astype(str))
        inputdata["Punctuality"]=label_encoder.transform([inputdata["Punctuality"]])[0]
        
        label_encoder.fit(in_df["Lying"].astype(str))
        inputdata["Lying"]=label_encoder.transform([inputdata["Lying"]])[0]
        
        label_encoder.fit(in_df["Important1"].astype(str))
        inputdata["Important1"]=label_encoder.transform([inputdata["Important1"]])[0]
        
        label_encoder.fit(in_df["Important2"].astype(str))
        inputdata["Important2"]=label_encoder.transform([inputdata["Important2"]])[0]
        
        label_encoder.fit(in_df["Important3"].astype(str))
        inputdata["Important3"]=label_encoder.transform([inputdata["Important3"]])[0]
        
        label_encoder.fit(in_df["Internet usage"].astype(str))
        inputdata["Internet usage"]=label_encoder.transform([inputdata["Internet usage"]])[0]
        
        inputdata=pd.DataFrame(inputdata, index=[0])
        res=random_forest.predict(inputdata)
        
        results={}
        results["Finances"]=res[0][4]
        results["Shopping centres"]=res[0][6]
        results["Branded clothing"]=res[0][1]
        results["Entertainment spending"]=res[0][3]
        results["Spending on looks"]=res[0][9]
        results["Spending on gadgets"]=res[0][7]
        results["Spending on healthy eating"]=res[0][8]
        results["Age"]=res[0][0]
        
        label_encoder.fit(out_df["Education"].astype(str))
        results["Education"]=label_encoder.inverse_transform(res[0][2].astype(int))
        
        label_encoder.fit(out_df["Village town"].astype(str))
        results["Village town"]=label_encoder.inverse_transform(res[0][10].astype(int))
        
        label_encoder.fit(out_df["House"].astype(str))
        results["House"]=label_encoder.inverse_transform(res[0][5].astype(int))
        return results



