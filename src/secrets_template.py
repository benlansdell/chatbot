import http 
import ssl

conn = http.client.HTTPSConnection("biogpt-1.cnvrg.stjude.org", 
                                   443, 
                                   context = ssl._create_unverified_context())

headers = {
    'Cnvrg-Api-Key': "XXXXXXXXXX",
    'Content-Type': "application/json"
    }

endpoint = "/api/v1/endpoints/XXXXXXXXXXXX"
