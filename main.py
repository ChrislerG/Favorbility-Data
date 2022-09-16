import csv 
import matplotlib.pyplot as plt

file = open("data.csv")#reads and opens data.csv 
csvreader = csv.reader(file)#creating a variable for csvreader
header = next(csvreader)#defining the header 
#print(header)
data = [] #empty list for data
for row in csvreader: #for loop putting row in csvreader
    data.append(row) #append data to row
#print(data)
file.close() #closes the opened files

poll_names = [] #empty list for poll_names

names = [] #empty list for names 
for i in range(len(data)): #for loop range/length of data

  names.append([data[i][0]]) #data indexes appended names

for i in range(len(names)): #for loop range/length of names
  
  if names[i] not in poll_names: #if statement for names list and pollnames 
    
    poll_names.append(names[i]) #names appended to poll_names 

#print(poll_names)

print() 

polls_dict = {} #empty key for polls_dict 

for i in range(len(poll_names)): #for loop range/length poll_names 

  polls_dict.update({poll_names[i][0]:[]}) #Updates polls_dict

#print(polls_dict) 
print() 

for i in range(len(data)): #for loop range/length of data
  values = data[i][1:] #defining values and making it equal to data 

  for key in polls_dict: #for loop for key in the pollis_dict 
   
    if data[i][0] == key: #if statement for data is equal to key 

      polls_dict[key].append(values) #appends polls_dict list to values 


#print(polls_dict) 



  
for key in polls_dict: #for loop for key in polls_dict list
  polls_dict[key].sort() #sorting the data in list 
  holder = [] #empty list for holder 
  
  for i in range(len(polls_dict[key])): #for loop for range/length of polls_dict[key] 
    if polls_dict[key][i][0][1].isnumeric(): #if statement to see if polls_dict list is numeric 
        holder.append(polls_dict[key][i]) #appending holder to polls_dict list

  for h in range(len(holder)): #for loop for range/length of holder
      polls_dict[key].append(holder[h]) #polls_dict list appended to holder

for j in range(len(holder)): #for loop for range/length of holder 
  if holder[j] in polls_dict[key]: #if statement for holder in polls_dict list
    polls_dict[key].remove(holder[j]) #removes holder from polls_dict



print(polls_dict) #prints list 

for key in polls_dict: #for loop for the key in polls_dict 

  plt.subplot(2, 1, 1) #creates a figure and a grid of subplots with a single call, while providing reasonable control over how the individual plots are created

  plt.title('Favorability') #Gives the data chart a title at the top 

  for i in range(len(polls_dict[key])): # for loop for plt.bar and plt.xticks

    plt.bar(polls_dict[key][i][0],polls_dict[key][i][1],color='blue') #changes color of the data bars 

  plt.xticks(rotation=90) # changes location/orientation 

  #plt.ylim(25,70)

  plt.grid() #Configures the grid lines

  plt.ylabel('Percentage of Population') #naming the y axis 

  plt.subplot(2,1,2) # #creates a figure and a grid of subplots with a single call, while providing reasonable control over how the individual plots are created

  plt.title('Unfavorability') #Gives the data chart a title at the top 

  for i in range(len(polls_dict[key])):  # for loop for plt.bar and plt.xticks

    plt.bar(polls_dict[key][i][0],polls_dict[key][i][2],color='red') #changes color of the data bars 

  plt.xticks(rotation=90) # changes location/orientation 

  #plt.ylim(25,70)

  plt.grid() #Configures the grid lines 

  plt.ylabel('Percentage of Population') #naming the y axis 

  plt.suptitle(key) #Add a centered suptitle to the figure

  plt.show(block=False) #Display all open figures

  plt.pause(5) #Run the GUI event loop for interval seconds

  plt.close() #Close a figure window




