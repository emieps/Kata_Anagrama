import pytest
import Ana as a 


@pytest.mark.parametrize(
   "lst, expect",
   [ 
      (['Hazelton', 'Hazleton', "Hazelton's", "Hazleton's", 'Heinz', 'Hizen','Helper', 'Hepler'], ['Hazelton', 'Hazleton']["Hazelton's", "Hazleton's"]['Heinz', 'Hizen']['Helper', 'Hepler']),
      (["Lenore", "Candice", "Chanel", "Chet", "Leroi", "Robbie", "Annalise",  "Ashleigh", "Jaxx"], 3, 3),  
      (["Deidre", "Tiffany", "Linzi", "Sheelagh", "Kaylani","Lawrence", "Dashiell", "Caitlin", "Guridi"], 4, 2)

   ]
)
