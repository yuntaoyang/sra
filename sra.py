#!/usr/bin/env python
# coding: utf-8

# # download sra and covert to fastq

# set up path

# In[1]:


# SraAccList file
SraAccList = '/home/yyang18/Project/SBMI_Zheng_NGS_Python_Script/SRA/SraAccList.txt'
# path to sra file
path_sra = '/data/yyang18/sra/'
# path to fastq file
path_fastq = '/data/yyang18/fastq/'
# name of logfile
log = 'logfile'


# In[2]:


import subprocess
import os
import logging
import pandas as pd


# In[3]:


sra_file = pd.read_csv(SraAccList,header=None)


# In[4]:


logging.basicConfig(level=logging.DEBUG, 
                        filename="logfile", 
                        filemode="a",
                        format="%(asctime)-15s %(levelname)-8s %(message)s")
logger = logging.getLogger(__name__)


# step1: create the directory of sra

# In[5]:


if os.path.isdir(path_sra):
    logger.info("File exists: "+path_sra)
else:
    os.mkdir(path_sra)
    logger.info("create the sra directory: "+path_sra)


# step2: create the directory of fastq

# In[6]:


if os.path.isdir(path_fastq):
    logger.info("File exists: "+path_fastq)
else:
    os.mkdir(path_fastq)
    logger.info("create the fastq directory: "+path_fastq)


# step3: download the sra files

# In[7]:


sra = 'prefetch -O . $(<'+      SraAccList+')'+' '+      '>'+' '+'sra.log'+' '+'2>&1'
process = subprocess.Popen(sra,shell=True,cwd=path_sra,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
process.communicate()
logging.info("sra download is done!")


# step4: convert sra files to fastq files

# In[8]:


for file in sra_file[0]:
    fastq_dump = 'fastq-dump --split-3'+' '+                 '--gzip'+' '+                  path_sra+file+'/'+file+'.sra'
    process = subprocess.Popen(fastq_dump,shell=True,cwd=path_fastq,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
    process.communicate()
    logging.info(file+" fastq-dump is done!")


# In[ ]:




