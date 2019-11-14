#pragma once

#include <iostream>

const int LEN = 10;
const int LEFT = 11;
const int RIGHT = 99;

int randomNumber(){
	return LEFT + rand() % (RIGHT - LEFT + 1);
}

void arrInit(int arr[], int len){
	for (int i = 0; i < len; ++i){
		arr[i] = randomNumber();
	}
}

void arrDisplay(int arr[], int len){
	for (int i = 0; i < len; ++i){
		std::cout << arr[i] << " ";
	}
	std::cout << std::endl;
}

void insertSort(int arr[], int len){
	int i, j, temp;
	for (i = 1; i < len; ++i){
		if (arr[i] < arr[i - 1]){
			temp = arr[i];
			for (j = i - 1; j >= 0 && arr[j] >= temp; --j){
				arr[j + 1] = arr[j];
			}
			arr[j + 1] = temp;
		}
	}
}

void shellSort(int arr[], int len){
	int i, j, k, gap, temp;
	for (gap = len / 2; gap > 0; gap /= 2){
		for (i = 0; i < gap; ++i){
			for (j = i + gap; j < len; j += gap){
				if (arr[j] < arr[j - gap]){
					temp = arr[j];
					for (k = j - gap; k >= 0 && arr[k] >= temp; k -= gap){
						arr[k + gap] = arr[k];
					}
					arr[k + gap] = temp;
				}
			}
		}
	}
}

void swap(int* a, int* b){
	int temp = *a;
	*a = *b;
	*b = temp;
}

void bubbleSort(int arr[], int len){
	for (int bound = 0; bound < len; ++bound){
		for (int cur = len - 1; cur > bound; --cur){
			if (arr[cur] < arr[cur - 1]){
				swap(&arr[cur], &arr[cur - 1]);
			}
		}
	}
}

void quickSort(int arr[], int left, int right){
	if (left > right){
		return;
	}

	int i = left;
	int j = right;
	int pivot = arr[left];
	while (i < j){
		while (i < j && arr[j] >= pivot){
			--j;
		}
		arr[i] = arr[j];

		while (i < j && arr[i] <= pivot){
			++i;
		}
		arr[j] = arr[i];
	}
	arr[i] = pivot;

	quickSort(arr, left, i - 1);
	quickSort(arr, i + 1, right);
}

void selectSort(int arr[], int len){
	int i, j, min;
	for (i = 0; i < len; ++i){
		min = i;
		for (j = i + 1; j < len; ++j){
			if (arr[j] < arr[min]){
				min = j;
			}
		}

		if (min != i){
			swap(&arr[i], &arr[min]);
		}
	}
}

void downAdjust(int arr[], int len, int root_index){
	int left_index = 2 * root_index + 1;
	if (left_index >= len){
		return;
	}

	int max_index = left_index;
	int right_index = 2 * root_index + 2;
	if (right_index < len && arr[right_index] > arr[max_index]){
		max_index = right_index;
	}

	if (arr[root_index] >= arr[max_index]){
		return;
	}

	swap(&arr[root_index], &arr[max_index]);

	downAdjust(arr, len, max_index);
}

void createHeap(int arr[], int len){
	for (int i = (len - 2) / 2; i >= 0; --i){
		downAdjust(arr, len, i);
	}
}

void heapSort(int arr[], int len){
	createHeap(arr, len);

	for (int i = 0; i < len; ++i){
		swap(&arr[0], &arr[len - 1 - i]);
		downAdjust(arr, len - 1 - i, 0);
	}
}

void merge(int arr[], int left, int mid, int right){
	int i = left, j = mid + 1, k = left;
	int* temp = (int*)malloc(sizeof(int) * (right + 1));

	while (i < mid + 1 && j < right + 1){
		if (arr[i] < arr[j]){
			temp[k++] = arr[i++];
		}
		else{
			temp[k++] = arr[j++];
		}
	}

	while (i < mid + 1){
		temp[k++] = arr[i++];
	}

	while (j < right + 1){
		temp[k++] = arr[j++];
	}

	for (i = left; i <= right; ++i){
		arr[i] = temp[i];
	}

	free(temp);
}

void mergeSort(int arr[], int left, int right){
	if (left < right){
		int mid = left + (right - left) / 2;
		mergeSort(arr, left, mid);
		mergeSort(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}
}

void SortTest(){
	int arr[LEN] = { 0 };

	arrInit(arr, LEN);

	printf("The origin array is: \n");
	arrDisplay(arr, LEN);

	mergeSort(arr, 0, LEN - 1);

	printf("The sorted array is:\n");
	arrDisplay(arr, LEN);
}