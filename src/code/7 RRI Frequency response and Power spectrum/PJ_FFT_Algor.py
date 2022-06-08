import ctypes
import os
from matplotlib import pyplot as plt
import numpy as np
from numpy.fft import fft, fftfreq


def get_ppi():
    '''get the dpi function'''
    LOGPIXELSX, user32 = (88, ctypes.windll.user32)

    user32.SetProcessDPIAware()
    dc = user32.GetDC(0)
    pix_per_inch = ctypes.windll.gdi32.GetDeviceCaps(dc, LOGPIXELSX)
    user32.ReleaseDC(0, dc)
    return pix_per_inch


def data_to_png(dataIn,
                dataOutPath: str,
                dataFileName: str,
                dpi: int = 100) -> None:
    """_summary_

    Args:
        dataIn (_type_): about the data in (like a list)
        dataOutPath (str): about the file output path
        dataFileName (str): about the picture file name 
        dpi (int, optional): control the picture output quality. Defaults to 100.
    """
    N, T = dataIn.size, 1.0 / 800.0  # f = 60 Hz

    # Create a signal
    x, y = np.linspace(0.0, N * T, N), dataIn
    yf = fft(y)

    # Where is a 200 Hz frequency in the results?
    freq = fftfreq(x.size, d=T)
    # Plot a spectrum
    plt.figure(figsize=(16, 12))

    plt.subplot(2, 2, 1)
    plt.plot(x, dataIn)
    plt.title('RRI spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('RRI values')
    plt.grid()

    # Amplitude spectrum
    plt.subplot(2, 2, 2)
    plt.semilogy(freq[0:N // 2], 2 / N * np.abs(yf[0:N // 2]))
    plt.title('Amplitude spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Magnitude (s)')
    plt.grid()

    # Phase spectrum
    plt.subplot(2, 2, 3)
    plt.plot(freq[0:N // 2], np.angle(yf[0:N // 2]))
    # plt.semilogy(freq[0:N // 2], np.angle(yf[0:N // 2]))
    plt.title('Phase spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('Phrase (rad)')
    plt.grid()

    # Power spectrum
    plt.subplot(2, 2, 4)
    xF = yf[0:N // 2]
    fr = np.linspace(0, 800 // 2, N // 2)
    plt.semilogy(fr, abs(xF)**2)
    plt.title('Power spectrum')
    plt.xlabel('Frequency (Hz)')
    plt.ylabel('PS D(s^2/Hz)')
    plt.grid()
    # plt.psd()

    #save file
    fileName = f'{dataFileName}.png'
    if not os.path.exists(dataOutPath):
        os.mkdir(dataOutPath)
    savePath = os.path.join(dataOutPath, fileName)

    plt.savefig(savePath, dpi=dpi)
