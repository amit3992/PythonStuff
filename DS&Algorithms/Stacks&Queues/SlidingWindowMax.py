from pythonds.basic import deque

def sliding_window_max(array, win_size):
    if win_size > len(array):
        return

    window = deque()

    # Find max of first window
    for i in range(0, win_size):
        while window and array[i] >= array[window[-1]]:
            window.pop()
        window.append(i)


    print(array[window[0]])

    for i in range(win_size, len(array)):
        #Remove all the numbers smaller than current number
        while window and array[i] >= array[window[-1]]:
            window.pop()

        #Remove first number if it doesn't fall in the window
        if window and (window[0] <= i - win_size):
            window.popleft()

        window.append(i)
        print(array[window[0]])


array = [-4,2,-5,-1,1,6]
sliding_window_max(array,3)
