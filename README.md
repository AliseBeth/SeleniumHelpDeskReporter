# SeleniumHelpDeskReporter

<i><b>Данный алгоритм создан для того, чтобы пробегать по списку заявок из еженедельного отчета и выявлять некорректно созданные/заполненные/направленные в не тот отдел.</b></i>

Основной алгоритм функционирования системы HelpDesk в компании заключается в следующем:
- пользователь пишет электронное письмо в профильный отдел
- письмо сортируется и выгружается в систему HelpDesk, присваиваясь профильной группе
- в профильной группе специалист берет эту заявку себе, отвечает на вопрос, его ответ из HelpDesk отправляется на почту пользователя

В итоге специалисты работают в системе HelpDesk, пользователи, в свою очередь, ведут всю переписку и получают информацию исключительно по почте.

<i>Из-за обилия заявок, еженедельно отправляемых отделом продаж, и человеческого фактора, который мешает сотрудникам отдела продаж корректно формулировать запросы специалистам HelpDesk, была выявлена необходимость быстро находить неверно заполненные заявки в их еженедельных выгрузках и проводить повторное обучение провинившихся. В ручном режиме быстро проверять 600+ заявок не представлялось возможным.</i>

<b>[!] Данные алгоритмы в вакууме не работают, так как из них убраны все ссылки и персональные данные пользователей. Во всех адресах почты домен также заменен.</b>

## SeleniumReporter
<i>- этот алгоритм, который пробегает по списку заявок из отчета </i>

Основные проблемы, которые которые может выявить данный алгоритм:

- отсутствие емейла получателя заявки в принципе
- запрос отправлен непрофильной группе
- запрос отправлен на ряд запретных технических емейлов
- запрос отправлен специалисту напрямую, минуя HelpDesk, и специалист был вынужден сам пересылать данный запрос в систему
- тема заявки оформлена неверно
- и так далее

## SeleniumSoloReporter
<i>- технический алгоритм, который проверяет только одну заявку (используется для поиска багов в свеженаписанном куске алгоритма или подозрительной заявке, на которой крашится предыдущий алгоритм) </i>