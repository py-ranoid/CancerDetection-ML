from django import forms
from django.utils.safestring import mark_safe

'''
class NameForm(forms.Form):
    #your_name : First Name
    your_name = forms.CharField(label=' First Name ',max_length=100,initial='Hello')
    last_name = forms.CharField(label='  Last Name  ',max_length=100)
    doc_id = forms.CharField(label=' Registered ID  ',max_length=100)
    salary = forms.IntegerField(label=' Salary         ')
'''

class NameForm(forms.Form):
    radius_mean = forms.FloatField(label=mark_safe(' Radius_Mean '))
    texture_mean = forms.FloatField(label=' Texture_Mean ')
    perimeter_mean = forms.FloatField(label=' Perimeter_Mean ')
    area_mean = forms.FloatField(label=' Area_Mean ')
    smoothness_mean = forms.FloatField(label=' Smoothness_Mean ')
    compactness_mean = forms.FloatField(label=' Compactness_Mean ')
    concavity_mean = forms.FloatField(label=' Concavity_Mean ')
    cancave_points_mean = forms.FloatField(label=' Concave Points_Mean ')
    symmetry_mean = forms.FloatField(label=' Symmetry_Mean ')
    fractal_dimension_mean = forms.FloatField(label=' Fractal_Dimension_Mean ')

    radius_se = forms.FloatField(label=' Radius_se ')
    texture_se = forms.FloatField(label=' texture_se ')
    perimeter_se = forms.FloatField(label=' Perimeter_se ')
    area_se = forms.FloatField(label=' Area_se ')
    smoothness_se = forms.FloatField(label=' Smoothness_se ')
    compactness_se = forms.FloatField(label=' Compactness_se ')
    concavity_se = forms.FloatField(label=' Concavity_se ')
    concave_points_se = forms.FloatField(label=' Concave Points_se ')
    symmetry_se = forms.FloatField(label=' Symmetry_se ')
    fractal_dimension_se = forms.FloatField(label=' Fractal_Dimension_se ')

    radius_worst = forms.FloatField(label=' Radius_worst ')
    texture_worst = forms.FloatField(label=' Texture_worst ')
    perimeter_worst = forms.FloatField(label=' Perimeter_worst ')
    area_worst = forms.FloatField(label=' Area_worst ')
    smoothness_worst = forms.FloatField(label=' Smoothnes_worst ')
    compactness_worst = forms.FloatField(label=' Compactness_worst ')
    concavity_worst = forms.FloatField(label=' Concavity_worst ')
    concave_points_worst = forms.FloatField(label=' Concave Points_worst ')
    symmetry_worst = forms.FloatField(label=' Symmetry_worst')
    fractal_dimension_worst = forms.FloatField(label=' Fractal_Dimension_worst ')
