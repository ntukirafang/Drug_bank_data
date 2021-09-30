import requests
import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import os
from time import sleep
import random
sleepMaxSeconds = 10 
sleepMinSeconds = 8
for i in range(4,255):
    page=str(i)
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
        'cookie': 'cf_chl_2=8b2868c55f18128; cf_chl_prog=a9; cf_clearance=C9N34f3icatjnErmpISxMiwyGx0iyoo37R6i.Ez6Jqk-1632281715-0-150; _omx_drug_bank_session=UVVpakRaY1dLZVdZYVc5NVN6eVN5ZEdXa3NDUDhsbnpFbWhMODRhT2Vkbkl0SHpGbEJVZWZJNGFqRjVhSmMxdTFUZTRCdHZDRnhOQ1gxWHR4VUpTWDd4R3oxMXhUeG55REx6cloxVXJoL3NoKytmSnpuVitSZ2EweUxyUTRTbi96VjlER0R4RzVJdU12SkF1RDdTd1JRPT0tLUx3UHM3VExiaVhMN0NabUJqdVdReXc9PQ%3D%3D--c800e55ff0ddf59cd82664ba04e73143ef64eb42',
    }
    url = 'https://go.drugbank.com/pharmaco/genomics?__cf_chl_jschl_tk__=pmd_cab7e84340fe8f46a0c6c68589db4494f143883b-1627271234-0-gqNtZGzNAiKjcnBszQlO&page={}'.format(page)
    resp = requests.get(url, headers=headers)
    soup = BeautifulSoup(resp.text, 'html.parser')
    dfs = pd.read_html(resp.text)
    print(dfs)
    dfs[0].to_csv(r'C:\Users\jimmy.fang\Desktop\SQL\page_{}.csv'.format(page),encoding="utf-8")
    sleep(random.randint(sleepMinSeconds, sleepMaxSeconds))
    df=pd.DataFrame()
for i in range(4,255):
    page=str(i)
    dfs=pd.read_csv(r'C:\Users\jimmy.fang\Desktop\SQL\page_{}.csv'.format(page),header=[0,1],index_col=0)
    df=df.append(dfs, ignore_index = True)
    
df=df.reset_index(drop=True)
df.columns = df.columns.map('_'.join)

df.columns=['Drug', 'Interacting Gene/Enzyme',\
       'Allele name', 'Genotypes','Defining change(s)','Type(s)',\
       'Description', 'Details']

col=['Drug', 'Interacting Gene/Enzyme',\
       'Allele name', 'Genotypes','Defining change(s)','Type(s)',\
       'Description']
df=df[col]
df.info()
df
df.to_csv(r'C:\Users\jimmy.fang\Desktop\SQL\Pharmaco_genomics_drug_bank.csv',encoding="utf-8")
