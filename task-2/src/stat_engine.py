import math
class StatEngine:
    def __init__(self, data):
        if not data:
            raise ValueError("Data cannot be empty.")

        self.data = self._clean_data(data)

        if len(self.data) == 0:
            raise ValueError("No valid numeric data found.")

    def _clean_data(self, data):
        cleaned = []
        for item in data:
            if isinstance(item, (int, float)):
                cleaned.append(item)
            elif isinstance(item, str):
                try:
                    cleaned.append(float(item))
                except ValueError:
                    continue
            else:
                continue
        return cleaned
    def get_mean(self):
        return sum(self.data) / len(self.data)
    def get_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2

        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]
    def get_mode(self):
        freq = {}

        for num in self.data:
            freq[num] = freq.get(num, 0) + 1

        max_count = max(freq.values())

        if max_count == 1:
            return "No mode (all values are unique)"

        modes = [k for k, v in freq.items() if v == max_count]
        return modes
    def get_variance(self, is_sample=True):
        n = len(self.data)

        if is_sample and n < 2:
            raise ValueError("Sample variance requires at least 2 data points.")

        mean = self.get_mean()

        squared_diffs = []
        for x in self.data:
            squared_diffs.append((x - mean) ** 2)

        if is_sample:
            return sum(squared_diffs) / (n - 1)   # Bessel’s correction
        else:
            return sum(squared_diffs) / n
    def get_standard_deviation(self, is_sample=True):
        variance = self.get_variance(is_sample)
        return math.sqrt(variance)
    def get_outliers(self, threshold=2):
        mean = self.get_mean()
        std_dev = self.get_standard_deviation()

        outliers = []

        for x in self.data:
            if abs(x - mean) > threshold * std_dev:
                outliers.append(x)

        return outliers