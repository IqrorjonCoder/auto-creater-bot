import functions
from functions import *


def main(rasm_id, raqam, guvohnoma_raqami, familiya, ism, ismi_sharifi, xona_raqami, sana):
    functions.writer_func(raqam, guvohnoma_raqami, familiya, ism, ismi_sharifi, xona_raqami, sana, rasm_id)
    fully_saved_image(rasm_id)


# main('AQAD1r8xG3IpEUp4', '55', '12324', 'islomov', 'iqrorjon', "iqboljon o'g'li", '1234', '24/22')
