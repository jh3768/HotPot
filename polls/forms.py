''' module form '''
from django import forms

class UploadFileForm(forms.Form):
    ''' form for upload file '''
    name = forms.CharField(max_length=50)
    pic = forms.ImageField()
    

    def getData(self, data):
    	mydata = self.cleaned_data[data]
    	return mydata
        