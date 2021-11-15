from PySide6.QtWidgets import QApplication, QGridLayout, QHBoxLayout, QLabel, QListWidget, QMainWindow, QVBoxLayout, QWidget, QPushButton

def cool_function():
    print("You clicked the magic button")

app = QApplication([])

# The main window is just a widget that will have a top level HBox in it.
main_window = QMainWindow()
central_wrapper = QWidget()
main_window.setCentralWidget(central_wrapper)

content_hbox = QHBoxLayout()
central_wrapper.setLayout(content_hbox)

# The main layout is two columns: The left nav/menu and the right library grid/view.
left_content = QVBoxLayout()
right_content = QVBoxLayout()
content_hbox.addLayout(left_content)
content_hbox.addLayout(right_content)

# Left content panel
header = QLabel("Manga Manager")
library_list = QListWidget()
add_library_btn = QPushButton("Add Library")
settings_btn = QPushButton("Settings")
left_content.addWidget(header)
left_content.addWidget(library_list)
left_content.addWidget(add_library_btn)
left_content.addWidget(settings_btn)

# Right content panel
upper_hbox = QHBoxLayout()
right_content.addLayout(upper_hbox)
library_label = QLabel("Library Name")
upper_hbox.addWidget(library_label)

button_hbox = QHBoxLayout()
upper_hbox.addLayout(button_hbox)
scan_btn = QPushButton("Scan Library")
update_btn = QPushButton("Update Library")
volume_btn = QPushButton("New Volumes")
button_hbox.addWidget(scan_btn)
button_hbox.addWidget(update_btn)
button_hbox.addWidget(volume_btn)

series_section = QGridLayout()
right_content.addLayout(series_section)


main_window.show()
app.exec()