from django.forms import ModelForm
from .models import Anomaly


class GeneralForm(ModelForm):
	class Meta:
		model = Anomaly
		fields = ['client', 'asset', 'component', 'sub_component', 'comments', 'criticality', 'code', 'image_1', 'image_1_description', 'image_2', 'image_2_description', 'video', 'video_description', 'anomaly_id', 'is_hist', 'hist_ref', 'inspector', 'coord', 'obcr']

class UpdateForm(ModelForm):
	class Meta:
		model = Anomaly
		fields = ['client', 'asset', 'component', 'sub_component', 'comments', 'criticality', 'code', 'image_1', 'image_1_description', 'image_2', 'image_2_description', 'video', 'video_description', 'anomaly_id', 'is_hist', 'hist_ref', 'inspector', 'coord', 'obcr', 'review_status', 'pdf_upload']
