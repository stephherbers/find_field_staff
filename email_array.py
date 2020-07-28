import pickle


def main():
    processed_email_array = [["nick@dimagi.com", "2011-05-19 14:05",  "Dodoma"],
     ["alex@dimagi.com", "2011-05-22 16:22",  "Lusaka"], ["alice@dimagi.com", "2019-12-21 17:05",  "Bangui"], ["bob@dimagi.com", "2019-12-21 17:05",  "Cambridge"],
      ["david@dimagi.com", "2019-12-21 17:05",  "Anapolis"],["cat@dimagi.com", "2019-12-21 17:05",  "Budapest"],
      ["sally@dimagi.com", "2019-12-21 17:05",  "Ponta Grosa"], ["sam@dimagi.com", "2019-12-21 17:05",  "Pires do Rio"],
      ["ada@dimagi.com", "2019-12-21 17:05",  "Kariba"], ["holly@dimagi.com", "2019-12-21 17:05",  "Gamboma"],
      ["emma@dimagi.com", "2019-12-21 17:05",  "Chicureo"], ["gray@dimagi.com", "2019-12-21 17:05",  "Chinhoyi"]]

      #["lisa@dimagi.com","2020-01-21 04:05", "Pretoria"],

    pickle.dump(processed_email_array, open( "processed_email_array.p", "wb"))

main()
