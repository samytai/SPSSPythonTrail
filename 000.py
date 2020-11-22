import spss, spssaux
print(spss.__version__)
spss.Submit("get file='C:\\Users\\sam\\Desktop\\Data202201119\\20201119_1047.sav'.")
spss.StartDataStep()
myDataset=spss.Dataset()
myVarlist=myDataset.varlist
print(len(myVarlist))
print(myVarlist)
for i in range(len(myVarlist)):
    print(str(i)+"--->"+spssaux.GetVariableNamesList()[i])
