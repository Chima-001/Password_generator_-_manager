import password_generator
import base64

class Password:
    def __init__(self, service, username, password):
        self.service = service
        self.username = username
        self.password = password

    def __str__(self):
        return f'Service: {self.service} | Username: {self.username} | Password: {self.password}'

    def get_service(self):
        return self.service
    
    def get_username(self):
        return self.username
    
    def get_password(self):
        return self.password
    
    def set_password(self, new_password):
        self.password = new_password
        

class PasswordVault:
    def __init__(self, master_password):
        self.master_password = master_password
        self.password_list = []

    def add_password(self, service, username, password):
        new_password = Password(service, username, password)
        self.password_list.append(new_password)

    def get_password(self, service):
        for i in self.password_list:

            if i.service == service:
                return i.password
            return None
        
    def list_services(self):
        for i in self.password_list:
            print(i.service)
    
    def generate(self):
        generated_password = password_generator.generate_password(12, 'y', 'y', 'y')
        return generated_password
    
    def save_to_file(self, filename = 'passwords.txt'):
        if not self.password_list:
            with open (filename, 'w') as file:
                file.write('')
            return f'No password added. Add a password to save.'
        
        else:
            with open (filename, 'w') as file:
                for i in self.password_list:
                    encrypted_password = self._encrypt(i.password)
                    file.write(f'{i.service},{i.username},{encrypted_password}\n')
            return f'Passwords saved successfully.'
            
    def load_file(self, filename = 'passwords.txt'):
        self.password_list = []

        try:
            with open(filename, 'r') as file:
                lines = file.readlines()

                for line in lines:
                    clean_line = line.strip()

                    if not line:
                        continue

                    new_line = clean_line.split(',')

                    if len(new_line) != 3:
                        print('Skipping malformed lines.')

                    service = new_line[0]
                    username = new_line[1]
                    password = self._decrypt(new_line[2])

                    new_password = Password(service, username, password)
                    self.password_list.append(new_password)
        
        except FileNotFoundError:
                print(f'No file found named {filename}.')

        except Exception as e:
                print(f'An unexpected error occured: {e}')

    def _encrypt(self, text):
        return base64.b64encode(text.encode()).decode()
    
    def _decrypt(self, encrypted_text):
        return base64.b64decode(encrypted_text.encode()).decode()

    def delete_password(self, service):
        for i in self.password_list:

            if i.service == service:
                self.password_list.remove(i)
                self.save_to_file(filename='passwords.txt')
                print(f'Password successfully deleted.')
                return
            
        print( f'Password service \'{service}\' not found.')

def main():
    print('\n===== PASSWORD MANAGER ======')

    while True:
        master = input('Enter master password or \'0\' to quit: ')
        vault = PasswordVault('master')

        if master == '0':
            break

        elif master != vault.master_password:
            print('Wrong password. Try again.')
            continue

        else:
            vault.load_file(filename='passwords.txt')

            while True:
                print('\n-- MENU OPTIONS --\n')
                print('1. Add Password\n2. Get Password\n3. List Services\n4. Generate Password\n5. View All Passwords\n6. Delete Password\n7. Save Password\n8. Exit')

                try:
                    user_choice = int(input('Enter an option (1-8): '))

                except ValueError:
                    print('Invalid input. Enter numbers (1-8)')
                    continue

                if user_choice == 1:
                    service = input('Enter password service: ')
                    username = input('Enter user name: ')
                    password = input('Enter password or \'g\' to generate password: ')

                    if password.lower() == 'g'.lower():
                        password = password_generator.generate_password(12, 'y', 'y', 'y')
                    
                    vault.add_password(service, username, password)
                    print(f'Password \'{password}\' has been successfully added.')
                    continue

                elif user_choice == 2:
                    if not vault.password_list:
                        print('No password stored. Add a password first.')
                        continue

                    service = input('Enter password service: ')
                    print(vault.get_password(service))
                    continue

                elif user_choice == 3:
                    if not vault.password_list:
                        print('No password stored. Add a password first.6')

                    else:
                        print('\nStored services:')
                        vault.list_services()
                        continue

                elif user_choice == 4:
                    print(vault.generate())
                    continue

                elif user_choice == 5:
                    if not vault.password_list:
                        print('No passwords available. Add a password first.')

                    for i in vault.password_list:
                        print(i)
                    continue

                elif user_choice == 6:
                    if not vault.password_list:
                        print(f'No password stored.')

                    else:
                        service = input('Enter password service: ')
                        vault.delete_password(service)
                        continue
                        
                elif user_choice == 7:
                    print(vault.save_to_file(filename='passwords.txt'))
                    continue

                elif user_choice == 8:
                    print('Exiting...')
                    return
                
                else:
                    print('Invalid input. Enter numbers (1-8): ')
                    continue
        

if __name__ == '__main__':
    main()