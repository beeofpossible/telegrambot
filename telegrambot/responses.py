from datetime import datetime

def sample_responses(input_text):
    user_message =str(input_text).lower()
    if user_message in ('hello', 'hi', "bonjour", "salut",):
        return('Hey, I am Love The RoBot ! What can I do for you sir?')

    if user_message in ('who are you', 'who are you?', "qui es-tu", "qui es-tu?",):
        return('Hey, I am Love The RoBot ! What can I do for you sir?')

    if user_message in ('time', "time?",):
        now= datetime.now()
        date_time= now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return("Actually, I have missed something... What did you say?")
