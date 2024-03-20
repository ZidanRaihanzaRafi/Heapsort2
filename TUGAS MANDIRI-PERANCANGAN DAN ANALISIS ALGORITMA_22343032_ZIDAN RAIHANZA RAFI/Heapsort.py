def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Membangun max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Melakukan penyortiran
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]  # Pindahkan elemen terbesar ke posisi terakhir yang belum diurutkan
        heapify(arr, i, 0)               # Memanggil heapify untuk memperbaiki struktur heap pada subarray yang belum diurutkan

# Contoh penggunaan
arr = [12, 11, 13, 5, 6, 7]
heapsort(arr)
print("Array yang telah diurutkan:", arr)
