
import pandas as pd, numpy as np
from collections import Counter

def CosinosSimilarity(Vec1,Vec2) :
    if len(Vec1)==len(Vec2) :
        d1d2 = sum(i[0] * i[1] for i in zip(Vec1, Vec2))
        ld1l = sum(i**2 for i in Vec1)**(.5)
        ld2l = sum(i**2 for i in Vec2)**(.5)
        return d1d2/ld1l*ld2l

farsi = 'فارسی'
arabic = 'عربی'
kurdi ='کردی'



ds = pd.read_excel("ST-HW1-Data.xlsx",sheet_name="Sheet1")
ds.columns = ['sentence','lang']
ds['sentence'] = ds['sentence'].str.strip()
CF = ds['sentence'].str.cat().replace(u'\u200c','').replace(u'\xa0','').replace(u"'",'')

CF = list(set(CF))

for i,char in enumerate(CF):
    ds['char '+str(i)] =  ds['sentence'].str.count(char)/ds['sentence'].str.len()
ds['tool'] = ds['sentence'].str.len()

#define Fractions
fractionsList = [[0.8, 0.2 , 0],[0.6, 0.2 , 0.2],[0.4, 0.2 , 0.4],[0.2, 0.2 , 0.6],[0 , 0.2 , 0.8]]
measures = {'Accuracy' : 0 , 'Precision' : 0 , 'Recall' : 0 , 'Fmeasure' : 0}
for i in range(5):
    fractions = np.array(fractionsList[i])

    # Arabic Train and Test
    df = ds[ds['lang']==arabic]
    # split into 3 parts
    trainArabic1,  testArabic , trainArabic2= np.array_split(
        df, (fractions[:-1].cumsum() * len(df)).astype(int))
    trainArabic = trainArabic1.append(trainArabic2, ignore_index=True)

    # Kurdi Train and Test
    df = ds[ds['lang']==kurdi]
    # split into 3 parts
    trainKurdi1, testKurdi, trainKurdi2 = np.array_split(
        df, (fractions[:-1].cumsum() * len(df)).astype(int))
    trainKurdi = trainKurdi1.append(trainKurdi2, ignore_index=True)

    # Farsi Train and Test
    df = ds[ds['lang']==farsi]
    # split into 3 parts
    trainFarsi1,  testFarsi , trainFarsi2 = np.array_split(
        df, (fractions[:-1].cumsum() * len(df)).astype(int))
    trainFarsi = trainFarsi1.append(trainFarsi2, ignore_index=True)

    train = pd.concat([trainArabic,trainFarsi, trainKurdi], ignore_index=True)
    test = pd.concat([testArabic,testFarsi, testKurdi], ignore_index=True)

    # Calculate Mean Vector for each language
    FarsiMeanVector = (trainFarsi.drop('sentence', axis=1).drop('lang', axis=1).drop('tool', axis=1).apply(lambda x: x.mean()))
    KurdiMeanVector = (trainKurdi.drop('sentence', axis=1).drop('lang', axis=1).drop('tool', axis=1).apply(lambda x: x.mean()))
    ArabicMeanVector = (trainArabic.drop('sentence', axis=1).drop('lang', axis=1).drop('tool', axis=1).apply(lambda x: x.mean()))

    predict = { 'FarsiTrue' : 0 , 'FarsiFalse': 0 ,'KurdiTrue' : 0 , 'KurdiFalse': 0 ,'ArabicTrue' : 0
                                                            , 'ArabicFalse': 0 , 'Unpredicted' : 0}
    predict['State'] = str(i + 1) + ' : ' + str(fractions)
    pred = []
    for index, row in test.drop('sentence', axis=1).drop('lang', axis=1).drop('tool', axis=1).iterrows():
        SimilarityToFarsi = CosinosSimilarity(list(row),FarsiMeanVector)
        SimilarityToKurdi = CosinosSimilarity(list(row), KurdiMeanVector)
        SimilarityToArabic = CosinosSimilarity(list(row), ArabicMeanVector)

        if SimilarityToFarsi > SimilarityToKurdi and SimilarityToFarsi > SimilarityToArabic :
            pred.append('Farsi')
            if test.iloc[index]['lang'] == farsi :
                predict['FarsiTrue'] += 1
            else:
                predict['FarsiFalse'] += 1
        elif SimilarityToKurdi > SimilarityToFarsi and SimilarityToKurdi > SimilarityToArabic :
            pred.append('Kurdi')
            if test.iloc[index]['lang'] == kurdi :
                predict['KurdiTrue'] += 1
            else:
                predict['KurdiFalse'] += 1

        elif SimilarityToArabic > SimilarityToFarsi and SimilarityToArabic > SimilarityToKurdi:
            pred.append('Arabic')
            if test.iloc[index]['lang'] == arabic:
                predict['ArabicTrue'] += 1
            else:
                predict['ArabicFalse'] += 1
        else:
            pred.append('Unpredicted')
            predict['Unpredicted'] += 1

    predict['Accuracy'] =  (predict['FarsiTrue'] + predict['KurdiTrue']+predict['ArabicTrue']) /\
                           (predict['FarsiTrue'] + predict['KurdiTrue']+predict['ArabicTrue']+predict['FarsiFalse'] + predict['KurdiFalse']+predict['ArabicFalse']+predict['Unpredicted'])

    epsilon = .0000000000000001
    predict['Precision'] = ( predict['FarsiTrue'] /(predict['FarsiTrue']  +predict['FarsiFalse']  +epsilon )+
                             predict['KurdiTrue'] /(predict['KurdiTrue']  +predict['KurdiFalse']  +epsilon )+
                             predict['ArabicTrue']/(predict['ArabicTrue'] +predict['ArabicFalse'] +epsilon )  ) / 3

    predict['Recall'] = ( predict['FarsiTrue'] / 10 +
                             predict['KurdiTrue'] /10 +
                             predict['ArabicTrue']/ 10
                          ) / 3

    predict['Fmeasure']=2*(predict['Precision']*predict['Recall'] )/(predict['Precision']+predict['Recall'] )

    with pd.ExcelWriter('3_'+str(i+1)+'.xlsx') as writer:
        ds.to_excel(writer, 'Dataset')
        train.to_excel(writer, 'Trainset')
        test.to_excel(writer, 'Testset')
        test['Predition'] = pred
        test.to_excel(writer, 'Testresult')
        pd.DataFrame.from_dict([predict]).to_excel(writer, 'Measures')
        writer.save()
    print(fractionsList[i],predict)
    measures['Accuracy'] += predict['Accuracy']
    measures['Precision'] += predict['Precision']
    measures['Recall'] += predict['Recall']
    measures['Fmeasure'] += predict['Fmeasure']


print('\n\n over all accuracy :',measures['Accuracy']/5,'\n over all Precision :',measures['Precision']/5,'\n over all Recall :',measures['Recall']/5,'\n over all Fmeasure :',measures['Fmeasure']/5)

import matplotlib.pyplot as plt;
plt.rcdefaults()
import matplotlib.pyplot as plt

objects = ('Accuracy', 'Precision', 'Recall', 'Fmeasure')
y_pos = np.arange(len(objects))
performance = [measures['Accuracy']/5,measures['Precision']/5, measures['Recall']/5,measures['Fmeasure']/5]

plt.bar(y_pos, performance, align='center', alpha=0.6)
plt.xticks(y_pos, objects)
plt.yticks(np.arange(0, 1.1, step=0.1))
plt.ylabel('precent')
plt.title('ANN course - HW1 - part C')

plt.show()