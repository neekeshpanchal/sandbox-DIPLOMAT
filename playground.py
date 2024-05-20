import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import re

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    best_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
        if best_index == -1 or abs(arr[mid] - target) < abs(arr[best_index] - target):
            best_index = mid
    return best_index

class DataAlignerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Neurophysiological Data Aligner")

        # Load SMI File Button
        self.load_smi_button = tk.Button(master, text="Load SMI File", command=self.load_smi)
        self.load_smi_button.pack()

        # Load Neuralynx CSV
        self.load_neuralynx_button = tk.Button(master, text="Load Neuralynx CSV", command=self.load_neuralynx)
        self.load_neuralynx_button.pack()

        # Align Data Button
        self.align_button = tk.Button(master, text="Align Data", command=self.align_data)
        self.align_button.pack()

        # Save Aligned Data Button
        self.save_button = tk.Button(master, text="Save Aligned Data", command=self.save_aligned_data)
        self.save_button.pack()

        # Plot Data Button
        self.plot_button = tk.Button(master, text="Plot Data", command=self.plot_data)
        self.plot_button.pack()

        self.smi_df = None
        self.neuralynx_df = None
        self.aligned_data = None

    def load_smi(self):
        filepath = filedialog.askopenfilename(filetypes=[("SMI Files", "*.smi")])
        if filepath:
            self.smi_df = self.parse_smi(filepath)
            print("SMI data loaded and processed.")

    def parse_smi(self, filepath):
        with open(filepath, 'r') as file:
            content = file.read()
        pattern = r"<SYNC Start=\d+><P Class=ENUSCC>(\d+)</SYNC>"
        matches = re.findall(pattern, content)
        frame_data = [(i + 1, int(timestamp) / 1000.0) for i, timestamp in enumerate(matches)]
        return pd.DataFrame(frame_data, columns=['Frame', 'PTime'])

    def load_neuralynx(self):
        filepath = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        if filepath:
            self.neuralynx_df = pd.read_csv(filepath)
            self.neuralynx_df['Timestamp'] = self.neuralynx_df['Timestamp'] / 1000.0
            print("Neuralynx CSV loaded and converted.")

    def align_data(self):
        if self.smi_df is None or self.neuralynx_df is None:
            messagebox.showerror("Error", "Load both files first.")
            return

        timestamps = self.neuralynx_df['Timestamp'].to_numpy()
        self.aligned_data = []
        for _, row in self.smi_df.iterrows():
            index = binary_search(timestamps, row['PTime'])
            self.aligned_data.append([row['Frame'], timestamps[index], self.neuralynx_df.iloc[index]['Signal']])

        self.aligned_data = pd.DataFrame(self.aligned_data, columns=['Frame', 'Aligned Timestamp', 'Signal'])
        print("Data aligned successfully.")

    def save_aligned_data(self):
        if self.aligned_data is not None:
            filepath = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV Files", "*.csv")])
            if filepath:
                self.aligned_data.to_csv(filepath, index=False)
                print("Aligned data saved to CSV successfully.")
        else:
            messagebox.showerror("Error", "No aligned data to save. Perform alignment first.")

    def plot_data(self):
        if self.aligned_data is None:
            messagebox.showerror("Error", "No data to plot. Perform alignment and save first.")
            return

        fig = make_subplots(rows=1, cols=1)
        fig.add_trace(go.Scatter(x=self.aligned_data['Aligned Timestamp'], y=self.aligned_data['Signal'], mode='lines+markers', name='Signal'), row=1, col=1)
        fig.update_layout(title_text="Neurophysiological Signal Over Time")
        fig.show()

root = tk.Tk()
app = DataAlignerGUI(root)
root.mainloop()
