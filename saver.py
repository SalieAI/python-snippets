'''
Short function using Pandas to export data from MongoDB to excel
'''
import pandas as pd
from pymongo import *

#connection to MongoDB
client = MongoClient('mongodb://localhost')

# Database
db = client.database

#Collection
collection = db.collection

def export_to_excel(name):
    '''
    save collection from MongoDB as .xlsx file, name of file is argument of function 
    '''
    data = list(collection.find({},{'_id':0}))
    df =  pd.DataFrame(data)
    writer = pd.ExcelWriter('{}.xlsx'.format(name), engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1')
    writer.save()
