import text
import veiw
import model
import text

def find_contacts(message):
    search_word = veiw.input_data(message)
    result = model.find_contact(search_word)
    veiw.show_contacts(result, text.find_contact_no_result(search_word))
    return True if result else False
def start_app():
    while True:
        user_choice = veiw.show_main_menu()
        match user_choice:
            case 1:
                model.open_phone_book()
                veiw.show_message(text.phone_book_opened_successfull)
            case 2:
                model.save_phone_book()
                veiw.show_message(text.phone_book_saved_successfull)
            case 3:
                veiw.show_contacts(model.phone_book, text.empty_phone_book_error)
            case 4:
                new_contact = veiw.input_data(text.input_new_contact)
                model.add_new_contact(new_contact)
                veiw.show_message(text.new_contact_added_successfull(new_contact[0]))
            case 5:
                find_contacts(text.input_search_word)
            case 6:
                if find_contacts(text.input_search_word_for_edit):
                    u_id = int(veiw.input_data(text.input_id_for_edit))
                    edited_contact = veiw.input_data(text.edit_contact)
                    name = model.edit_contact(u_id,edited_contact)
                    veiw.show_message(text.edit_contact_successful(name))
            case 7:
                if find_contacts(text.input_search_word_for_delete):
                    u_id = int(veiw.input_data(text.input_id_for_delete))
                    name = model.delete_contact(u_id)
                    veiw.show_message(text.delete_contact_successful(name))
            case 8:
                if find_contacts(text.input_search_word_for_copy):
                    u_id = int(veiw.input_data(text.input_id_for_copy))
                    model.copy_to_another_file(u_id)
                    name = model.copy_to_another_file(u_id)
                    veiw.show_message(text.copy_contact_successful(name))
            case 9:
                brake
