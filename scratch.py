# generate a code that can create a jsonl file for training. look at the customer_support_tickets.csv. Each json should contain a prompt and completion keys. for prompt combine the 
# the ticket subject and ticket description and for completion use the ticket type. select 100 rows per ticket type and shuffle the data.
# save the data as train.jsonl

import pandas as pd
import json
import random

df = pd.read_csv('customer_support_tickets.csv')
df = df[['Ticket Type', 'Ticket Subject', 'Ticket Description']]
df = df.dropna()
df = df.reset_index(drop=True)

df.columns = df.columns.str.replace(' ', '_').str.lower()

df['prompt'] = " Subject: " + df['ticket_subject'] + ", Body: " + df['ticket_description']
df['completion'] = df['ticket_type']

df = df[['prompt', 'completion']]

df = df.sample(frac=1).reset_index(drop=True)

# get 100 random samples for each ticket_type and shuffle the data


print(df.shape)
exit()

df.to_json('train.jsonl', orient='records', lines=True)

