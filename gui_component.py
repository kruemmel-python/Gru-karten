# gui_component.py
# This file is part of the PySide6 GUI component for the Greeting Card Generator.
# It is licensed under the LGPL license.

from PySide6.QtWidgets import (QWidget, QLabel, QVBoxLayout, QTextEdit, QComboBox, QPushButton, QColorDialog, QFontComboBox, QSpinBox, QDialog, QCheckBox)
from PySide6.QtGui import QColor, QImage, QPainter, QPen, QFont, QPolygonF, QPixmap
from PySide6.QtCore import Qt, QPointF

class PreviewDialog(QDialog):
    def __init__(self, image, parent=None):
        super().__init__(parent)
        self.initUI(image)
    
    def initUI(self, image):
        self.setWindowTitle('Greeting Card Preview')
        
        layout = QVBoxLayout()
        
        self.image_label = QLabel(self)
        pixmap = QPixmap.fromImage(image)
        self.image_label.setPixmap(pixmap)
        layout.addWidget(self.image_label)
        
        self.setLayout(layout)
        self.setGeometry(300, 300, 800, 600)

class GreetingCardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Greeting Card Generator')
        
        layout = QVBoxLayout()

        # Grußkartentext
        self.label_text = QLabel('Greeting Text:')
        layout.addWidget(self.label_text)
        
        self.text_entry = QTextEdit(self)
        layout.addWidget(self.text_entry)
        
        # Schriftart-Auswahl
        self.label_font = QLabel('Select Font:')
        layout.addWidget(self.label_font)
        
        self.font_combo = QFontComboBox(self)
        layout.addWidget(self.font_combo)
        
        # Schriftgröße-Auswahl
        self.label_font_size = QLabel('Select Font Size:')
        layout.addWidget(self.label_font_size)
        
        self.font_size_spinbox = QSpinBox(self)
        self.font_size_spinbox.setRange(10, 100)
        self.font_size_spinbox.setValue(20)
        layout.addWidget(self.font_size_spinbox)
        
        # Schriftfarbe-Auswahl
        self.label_font_color = QLabel('Select Font Color:')
        layout.addWidget(self.label_font_color)
        
        self.font_color_button = QPushButton('Choose Font Color', self)
        layout.addWidget(self.font_color_button)
        
        # Textausrichtung
        self.label_align = QLabel('Select Text Alignment:')
        layout.addWidget(self.label_align)
        
        self.align_combo = QComboBox(self)
        self.align_combo.addItems(["Left", "Center", "Right", "Justify"])
        layout.addWidget(self.align_combo)
        
        # Auswahl des Designs
        self.label_design = QLabel('Select Design:')
        layout.addWidget(self.label_design)
        
        self.designs = ["Text-based", "Stars and Clouds", "Frame"]
        self.design_combo = QComboBox(self)
        self.design_combo.addItems(self.designs)
        layout.addWidget(self.design_combo)

        # Auswahl des Rahmentyps
        self.label_frame_type = QLabel('Select Frame Type:')
        layout.addWidget(self.label_frame_type)
        
        self.frame_types = ["Straight", "Zigzag", "Wavy", "Looped"]
        self.frame_combo = QComboBox(self)
        self.frame_combo.addItems(self.frame_types)
        layout.addWidget(self.frame_combo)

        # Rahmenfarbe-Auswahl
        self.label_frame_color = QLabel('Select Frame Color:')
        layout.addWidget(self.label_frame_color)
        
        self.frame_color_button = QPushButton('Choose Frame Color', self)
        layout.addWidget(self.frame_color_button)
        
        # Checkbox für Schatten
        self.shadow_checkbox = QCheckBox("Add Shadow to Frame", self)
        layout.addWidget(self.shadow_checkbox)

        # Checkbox für Kombination
        self.combine_checkbox = QCheckBox("Apply both Design and Frame", self)
        layout.addWidget(self.combine_checkbox)
        
        # Farbwahl
        self.label_color = QLabel('Select Background Color:')
        layout.addWidget(self.label_color)
        
        self.color_button = QPushButton('Choose Background Color', self)
        layout.addWidget(self.color_button)

        self.preview_button = QPushButton('Preview Greeting Card', self)
        layout.addWidget(self.preview_button)
        
        self.create_button = QPushButton('Create Greeting Card', self)
        layout.addWidget(self.create_button)

        self.setLayout(layout)
        self.setGeometry(300, 300, 400, 600)
    
    def connect_signals(self, choose_color_func, choose_font_color_func, choose_frame_color_func, preview_greeting_card_func, create_greeting_card_func):
        self.color_button.clicked.connect(choose_color_func)
        self.font_color_button.clicked.connect(choose_font_color_func)
        self.frame_color_button.clicked.connect(choose_frame_color_func)
        self.preview_button.clicked.connect(preview_greeting_card_func)
        self.create_button.clicked.connect(create_greeting_card_func)
