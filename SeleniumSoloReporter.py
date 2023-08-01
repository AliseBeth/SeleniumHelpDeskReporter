from selenium import webdriver
from selenium.webdriver.common.by import By



link1 = "ссылка на HelpDesk"
link2 = "ссылка на одну заявку, которую будем проверять"
a = 0
key_words = ['приёмка', 'приемка', 'приемку', 'приёмку', 'приёмке', 'приемке', 'пути', 'впути', 'россия', 'семенова', 'иванова', 'петрова']
key_words_priemka = ['приёмка', 'приемка', 'приемку', 'приёмку', 'приёмке', 'приемке', 'приёмки', 'приемки']
key_words_vputi = ['пути', 'впути']
key_words_russia = ['россия', 'семенова', 'иванова', 'петрова']

specialist_priemka = ['Сидорова Анна']
specialist_vputi = ['Спиридонов Вадим']
specialist_russia = ['Семенова Наталья', 'Иванова Елена', 'Петрова Мария']


caution_emails = ['список емейлов, на которые нельзя писать заявки']
check_product = ['артикул', 'арт']

browser = webdriver.Chrome()
browser.implicitly_wait(10)
browser.get(link1)
browser.find_element(By.ID, 'username').send_keys('логин')
browser.find_element(By.ID, 'password').send_keys('пароль')
browser.find_element(By.ID, 'loginSDPage').click()


#из-за человеконенавистнической специфики верстки сайта HelpDesk далее часто будет использоваться поиск по Xpath, прошу понять и простить
browser.get(link2)
request_id = browser.find_element(By.ID, "request-id").text
title = browser.find_element(By.XPATH, "//span[@id='req-subject']").text.lower()
specialist = browser.find_element(By.XPATH, "// div[@id='technician-right-panel'] /p[@class='form-control-static spot-static colon']").text

try:
    user_1 = browser.find_element(By.XPATH, "//div[@id='desc-body'] /div /div /span /span").text

    user_2 = browser.find_element(By.XPATH, "// div[@id='group-right-panel'] /p[@class='form-control-static spot-static colon']").text.lower()



    while a == 0:
            if 'admins@email.ru' in user_1 and user_2 == 'it-help':
                break
            if user_1 == 'claims@email.ru':
                print(request_id, user_1, user_2, "------", 'ТАКОГО АДРЕСА НЕ СУЩЕСТВУЕТ')
                break
            if user_2 in user_1:
                looking_for_emails = list(filter(lambda i: i in user_1, caution_emails))
                if looking_for_emails == []:
                    if 'claim@email.ru' in user_1:
                        number_emails = user_1.count('help@email.ru') + 1

                        if number_emails == 1:
                            break

                        if number_emails > 1:
                            if 'admins@email.ru' in user_1 and user_2 == 'it-help':
                                print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                break
                            if user_2 == 'supply-help':
                                simular_words = list(filter(lambda i: i in title, key_words))
                                simular_words_pr = list(filter(lambda i: i in title, key_words_priemka))
                                simular_words_vp = list(filter(lambda i: i in title, key_words_vputi))
                                simular_words_ru = list(filter(lambda i: i in title, key_words_russia))

                                if simular_words_pr != [] and specialist in specialist_priemka:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break
                                if simular_words_vp != [] and specialist in specialist_vputi:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break
                                if simular_words_ru != [] and specialist in specialist_russia:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break

                                else:
                                    print(request_id, user_1, '"', title,'" ', specialist, "------", 'Неверная тема заявки + НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break

                            if user_1 == 'it-help@email.ru':
                                print(request_id, user_1, "------", 'Написали на IT + НЕСКОЛЬКО ЕМЕЙЛОВ')
                                break
                            if user_2 == 'product-help':
                                looking_for_product = list(filter(lambda i: i in title, check_product))
                                if looking_for_product != []:
                                    break
                                else:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + ПРОВЕРИТЬ ТЕМУ: ', title)
                                    break
                            else:
                                print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                break


                    else:
                        number_emails = user_1.count('help@email.ru')
                        if number_emails == 1:

                            if user_2 == 'supply-help':
                                simular_words = list(filter(lambda i: i in title, key_words))
                                simular_words_pr = list(filter(lambda i: i in title, key_words_priemka))
                                simular_words_vp = list(filter(lambda i: i in title, key_words_vputi))
                                simular_words_ru = list(filter(lambda i: i in title, key_words_russia))

                                if simular_words_pr != [] and specialist in specialist_priemka:
                                    break
                                if simular_words_vp != [] and specialist in specialist_vputi:
                                    break
                                if simular_words_ru != [] and specialist in specialist_russia:
                                    break

                                else:
                                    print(request_id, user_2, '"', title,'" ', specialist, "------", 'Неверная тема заявки')
                                    break

                            if 'it-help@email.ru' in user_1:
                                print(request_id, user_1, user_2, "------", 'Написали на IT')
                                break
                            if user_2 == 'product-help':
                                looking_for_product = list(filter(lambda i: i in title, check_product))
                                if looking_for_product != []:
                                    break
                                else:
                                    print(request_id, user_2, "------", 'ПРОВЕРИТЬ ТЕМУ: ', title)
                                    break

                            else:
                                break

                        if number_emails > 1:
                            if 'admins@email.ru' in user_1 and user_2 == 'it-help':
                                print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                break
                            if user_2 == 'supply-help':
                                simular_words = list(filter(lambda i: i in title, key_words))
                                simular_words_pr = list(filter(lambda i: i in title, key_words_priemka))
                                simular_words_vp = list(filter(lambda i: i in title, key_words_vputi))
                                simular_words_ru = list(filter(lambda i: i in title, key_words_russia))

                                if simular_words_pr != [] and specialist in specialist_priemka:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break
                                if simular_words_vp != [] and specialist in specialist_vputi:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break
                                if simular_words_ru != [] and specialist in specialist_russia:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break

                                else:
                                    print(request_id, user_1, '"', title, '" ', specialist, "------",
                                          'Неверная тема заявки + НЕСКОЛЬКО ЕМЕЙЛОВ')
                                    break

                            if user_1 == 'it-help@email.ru':
                                print(request_id, user_1, "------", 'Написали на IT + НЕСКОЛЬКО ЕМЕЙЛОВ')
                                break
                            if user_2 == 'product-help':
                                looking_for_product = list(filter(lambda i: i in title, check_product))
                                if looking_for_product != []:
                                    break
                                else:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + ПРОВЕРИТЬ ТЕМУ: ', title)
                                    break
                            else:
                                print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ')
                                break
                else:
                    if 'claim@email.ru' in user_1:
                        number_emails = user_1.count('help@email.ru') + 1

                        if number_emails == 1:
                            print(request_id, user_1, "------", 'Найдены личные емейлы: ',
                                  looking_for_emails)
                            break


                        if number_emails > 1:

                            if user_2 == 'supply-help':
                                simular_words = list(filter(lambda i: i in title, key_words))
                                simular_words_pr = list(filter(lambda i: i in title, key_words_priemka))
                                simular_words_vp = list(filter(lambda i: i in title, key_words_vputi))
                                simular_words_ru = list(filter(lambda i: i in title, key_words_russia))

                                if simular_words_pr != [] and specialist in specialist_priemka:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                    break
                                if simular_words_vp != [] and specialist in specialist_vputi:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                    break
                                if simular_words_ru != [] and specialist in specialist_russia:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                    break

                                else:
                                    print(request_id, user_1, '"', title, '" ', specialist, "------",
                                          'Неверная тема заявки + НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                    break

                            if user_1 == 'it-help@email.ru':
                                print(request_id, user_1, "------", 'Написали на IT + НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                break
                            if user_2 == 'product-help':
                                looking_for_product = list(filter(lambda i: i in title, check_product))
                                if looking_for_product != []:
                                    break
                                else:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + ПРОВЕРИТЬ ТЕМУ: ', title, 'Найдены личные емейлы: ',
                                      looking_for_emails)
                                    break
                            else:
                                print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                break


                    else:
                        number_emails = user_1.count('help@email.ru')

                        if number_emails == 1:

                            if user_2 == 'supply-help':
                                simular_words = list(filter(lambda i: i in title, key_words))
                                simular_words_pr = list(filter(lambda i: i in title, key_words_priemka))
                                simular_words_vp = list(filter(lambda i: i in title, key_words_vputi))
                                simular_words_ru = list(filter(lambda i: i in title, key_words_russia))

                                if simular_words_pr != [] and specialist in specialist_priemka:
                                    print(request_id, user_1, "------", 'Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break
                                if simular_words_vp != [] and specialist in specialist_vputi:
                                    print(request_id, user_1, "------", 'Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break
                                if simular_words_ru != [] and specialist in specialist_russia:
                                    print(request_id, user_1, "------", 'Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break

                                else:
                                    print(request_id, user_2, '"', title, '" ', specialist, "------",
                                          'Неверная тема заявки + Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break

                            if 'it-help@email.ru' in user_1:
                                print(request_id, user_1, user_2, "------", 'Написали на IT + Найдены личные емейлы: ',
                                      looking_for_emails)
                                break
                            if user_2 == 'product-help':
                                looking_for_product = list(filter(lambda i: i in title, check_product))
                                if looking_for_product != []:
                                    break
                                else:
                                    print(request_id, user_2, "------", 'ПРОВЕРИТЬ ТЕМУ: ', title,
                                          '+ Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break

                            else:
                                print(request_id, user_1, "------", 'Найдены личные емейлы: ',
                                      looking_for_emails)
                                break

                        if number_emails > 1:

                            if user_2 == 'supply-help':
                                simular_words = list(filter(lambda i: i in title, key_words))
                                simular_words_pr = list(filter(lambda i: i in title, key_words_priemka))
                                simular_words_vp = list(filter(lambda i: i in title, key_words_vputi))
                                simular_words_ru = list(filter(lambda i: i in title, key_words_russia))

                                if simular_words_pr != [] and specialist in specialist_priemka:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break
                                if simular_words_vp != [] and specialist in specialist_vputi:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break
                                if simular_words_ru != [] and specialist in specialist_russia:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break

                                else:
                                    print(request_id, user_1, '"', title, '" ', specialist, "------",
                                          'Неверная тема заявки + НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break

                            if user_1 == 'it-help@email.ru':
                                print(request_id, user_1, "------",
                                      'Написали на IT + НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                break
                            if user_2 == 'product-help':
                                looking_for_product = list(filter(lambda i: i in title, check_product))
                                if looking_for_product != []:
                                    break
                                else:
                                    print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + ПРОВЕРИТЬ ТЕМУ: ', title,
                                          'Найдены личные емейлы: ',
                                          looking_for_emails)
                                    break
                            else:
                                print(request_id, user_1, "------", 'НЕСКОЛЬКО ЕМЕЙЛОВ + Найдены личные емейлы: ',
                                      looking_for_emails)
                                break


            else:
                looking_for_emails = list(filter(lambda i: i in user_1, caution_emails))
                if looking_for_emails == []:
                    print(request_id, user_1, user_2, "------", 'Неверный адрес запроса')
                    break
                else:
                    print(request_id, user_1, user_2, "------", 'Неверный адрес запроса + Найдены личные емейлы: ',
                                  looking_for_emails)
                    break
except:
    print(request_id, '----- Что-то не так с адресом заявки (скорее всего ее создавали из другой заявки)')



old_window = browser.window_handles[0]
browser.close()


browser.quit()
