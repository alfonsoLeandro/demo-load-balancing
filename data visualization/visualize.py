import xml.etree.ElementTree as ET
import matplotlib.pyplot as plt

# Parse the XML file
root = ET.parse('../jmeter/jmeter_results.xml').getroot()

# Extract all response bodies
responses = dict()
for sample in root.findall('httpSample'):
    response_data = sample.find('responseData').text
    if response_data not in responses:
        responses[response_data] = 0
    responses[response_data] += 1


# Prepare data for the pie chart
labels = list(responses.keys())
sizes = list(responses.values())

# Plot the pie chart
plt.figure(figsize=(6, 6))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=['lightblue', 'lightgreen', 'lightcoral'])
plt.title('Distribución relativa de respuestas')
plt.show()