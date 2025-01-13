import os.path
from selene import browser, by, have

first_name = 'Nikita'
last_name = 'Ivanov'
user_email = 'nikitaivanov@email.com'
gender = 'Male'
user_number = '7902453219'
birth_year = '1996'
birth_month = 'February'
birth_day = '13'
subjects_type = 'Chemistry'
hobbies = 'Sports'
upload_picture = '123.jpeg'
current_address = 'Moscow, Lenina street, 9'
state = 'Haryana'
city = 'Panipat'

def test_homework5():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.execute_script("$('#fixedban').remove()")
    browser.driver.execute_script("$('footer').remove()")
    browser.element('#firstName').type(first_name)
    browser.element('#lastName').type(last_name)
    browser.element('#userEmail').type(user_email)
    browser.element('label[for="gender-radio-1"]').click()
    browser.element('#userNumber').type(user_number)
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('[value = "1996"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value = "1"]').click()
    browser.element('.react-datepicker__day--013').click()
    browser.element('#subjectsInput').type(subjects_type).press_enter()
    browser.element('label[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.path.abspath(upload_picture))
    browser.element('#currentAddress').type(current_address)
    browser.element('#state').click().element(by.text(state)).click()
    browser.element('#city').click().element(by.text(city)).click()
    browser.element('#submit').click()

    browser.element('.modal-content').should(have.text('Student Name')).should(have.text((first_name + ' ' + last_name).strip()))
    browser.element('.modal-content').should(have.text('Student Email')).should(have.text(user_email))
    browser.element('.modal-content').should(have.text('Gender')).should(have.text(gender))
    browser.element('.modal-content').should(have.text('Mobile')).should(have.text(user_number))
    browser.element('.modal-content').should(have.text('Date of Birth')).should(have.text((birth_day) + ' ' + (birth_month) + ',' + (birth_year)))
    browser.element('.modal-content').should(have.text('Subjects')).should(have.text(subjects_type))
    browser.element('.modal-content').should(have.text('Hobbies')).should(have.text(hobbies))
    browser.element('.modal-content').should(have.text('Picture')).should(have.text(upload_picture))
    browser.element('.modal-content').should(have.text('Address')).should(have.text(current_address))
    browser.element('.modal-content').should(have.text('State and City')).should(have.text((state) + ' ' + (city)))

