# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 13:40:56 2018

@author: user
"""
import MySQLdb
import pandas as pd
con=MySQLdb.connect(host='127.0.0.1', port=3306, user='root', db='csv_db', charset='utf8')
cur=con.cursor()
cur.execute("SELECT * FROM after_svm")
data=cur.fetchall()
tanggalan=[]
for d in data:
    if d not in tanggalan:
        tanggalan.append(d[1])
con.commit()
con.close()

#info : bentuk data : ID_STR, TANGGAL, KELAS MANUAL, KELAS LINEAR, KELAS POLY, KELAS RBF, KELAS SIG
y_positive=0
y_negative=0
data=[]
for tanggal in tanggalan:
    for d in data:
        if tanggal==d[1]:
            if d[3]=='positive':
                y_positive+=1
            elif d[3]=='negative':
                y_negative+=1
    
    data.append([tanggal,y_positive,y_negative])

xy=pd.DataFrame(data)
x=xy[0]
y_pos=xy[1]
y_neg=xy[2]
from sklearn.svm import SVR

svr_lin_pos=SVR(kernel='linear')
svr_lin_neg=SVR(kernel='linear')
svr_rbf_pos=SVR(kernel='rbf')
svr_rbf_neg=SVR(kernel='rbf')
svr_poly_pos=SVR(kernel='poly')
svr_poly_neg=SVR(kernel='poly')

svr_lin_pos.fit(x,y_pos)
svr_rbf_pos.fit(x,y_pos)
svr_poly_pos.fit(x,y_pos)
svr_lin_neg.fit(x,y_neg)
svr_rbf_neg.fit(x,y_neg)
svr_poly_neg.fit(x,y_neg)

import pickle
savlinpos='linear_positive.sav'
savrbfpos='rbf_positive.sav'
savpolypos='poly_positive.sav'

savlinneg='linear_negative.sav'
savrbfneg='rbf_negative.sav'
savpolyneg='poly_negative.sav'

pickle.dump(svr_lin_pos,open(savlinpos,'wb'))
pickle.dump(svr_rbf_pos,open(savrbfpos,'wb'))
pickle.dump(svr_poly_pos,open(savpolypos,'wb'))

pickle.dump(svr_lin_neg,open(savlinneg,'wb'))
pickle.dump(svr_rbf_neg,open(savrbfneg,'wb'))
pickle.dump(svr_poly_neg,open(savpolyneg,'wb'))

#//////////////////////////////////////////////////////////////////////////////

#test_lin_pos=pickle.load(open(savlinpos,'rb'))
#test_rbf_pos=pickle.load(open(savrbfpos,'rb'))
#test_poly_pos=pickle.load(open(savpolypos,'rb'))
#
#test_lin_neg=pickle.load(open(savlinneg,'rb'))
#test_rbf_neg=pickle.load(open(savrbfneg,'rb'))
#test_poly_neg=pickle.load(open(savpolyneg,'rb'))


y_lin_pos=svr_lin_pos.predict(x)
y_rbf_pos=svr_rbf_pos.predict(x)
y_poly_pos=svr_poly_pos.predict(x)

y_lin_neg=svr_lin_neg.predict(x)
y_rbf_neg=svr_rbf_neg.predict(x)
y_poly_neg=svr_poly_neg.predict(x)
