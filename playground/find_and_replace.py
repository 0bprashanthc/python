import os,sys
import glob
import pprint
packages=filter(os.path.isdir,os.listdir(os.getcwd()))
for i in range (0,len(packages)):
	yang_files=glob.glob(packages[i]+"/src/yang/*.yang")
	for j in range(0,len(yang_files)):
		os.system("sed -i -e 's/module "+yang_files[j].split('/')[3].split('.')[0]+"/module services-b2b-bycisco-"+yang_files[j].split('/')[3].split('.')[0]+"/g' "+yang_files[j])
		os.system("sed -i -e 's/prefix "+yang_files[j].split('/')[3].split('.')[0]+"/prefix services-b2b-bycisco-"+yang_files[j].split('/')[3].split('.')[0]+"/g' "+yang_files[j])
		os.system("sed -i -e 's/ncs:servicepoint "+yang_files[j].split('/')[3].split('.')[0]+"-servicepoint/ncs:servicepoint services-b2b-bycisco-"+yang_files[j].split('/')[3].split('.')[0]+"-servicepoint/g' "+yang_files[j])
		os.system("sed -i -e 's/namespace \"http:\/\/fr\/sfr\/"+yang_files[j].split('/')[3].split('.')[0]+"\"/namespace \"http:\/\/services.b2b.bycisco.sfr.com\/"+yang_files[j].split('/')[3].split('.')[0]+"\"/g' "+yang_files[j])
		os.system("sed -i -e 's/namespace \"http:\/\/com\/example\/"+yang_files[j].split('/')[3].split('.')[0]+"\"/namespace \"http:\/\/services.b2b.bycisco.sfr.com\/"+yang_files[j].split('/')[3].split('.')[0]+"\"/g' "+yang_files[j])
		os.rename(yang_files[j],packages[i]+"/src/yang/services-b2b-bycisco-"+yang_files[j].split('/')[3])
	xml_files=glob.glob(packages[i]+"/templates/*.xml")
	for j in range(0,len(xml_files)):
		os.rename(xml_files[j],packages[i]+"/templates/services-b2b-bycisco-"+xml_files[j].split('/')[2])
	os.system("sed -i -e 's/<name>"+packages[i]+"<\/name>/<name>services-b2b-bycisco-"+packages[i]+"<\/name>/g' "+packages[i]+"/package-meta-data.xml")
	os.rename(packages[i],"services-b2b-bycisco-"+packages[i])
