# Signal and system Final Project 2022
#### Written by KYLiN and MP Liew

---

## Master
We are using `Python` and `LabView` to develop the final project 

----
## Download 
#### ***Zip***
You can click `Code` -> `Download Zip` to download a zip file

#### ***Git*** 

You can download using git , copy this command 

`git clone https://github.com/KeithLin724/Signal-and-system-final-project-2022`

----
# Flow Chart

```mermaid
flowchart 
%% pkg
    subgraph pkg 
        FileCenter
        FileDataClass
    end

%% freq 
    subgraph Frequency_response_and_Power_spectrum
        PowerSpectrum
        Frequency_response_and_Power_spectrum_To_png
    end

%% main
    start
    subgraph Make_setup_path
        Folder_code-->filter_code-->Draw_wave_form
    end
    start-->Make_setup_path

%% Index different with original 
    
    subgraph index_compare_HR_output
        index_to_HR_with_HR_File_Diff
        index_to_HR_with_HR_File_Diff_picture
    end

    Make_setup_path-->index_compare_HR
    pkg-.->index_compare_HR-->index_compare_HR_output

%% Find RR Wave form
    
    subgraph RRI_code
        Find_RR_Waveform
        Find_RR_Waveform_method2
    end

    index_compare_HR-->RRI_code
    pkg-.->RRI_code-->RRI_output_file

%% SV plot 
    pkg-.->plot_graph_SV-->Output_SV_graphs
    RRI_code-->plot_graph_SV

%% RRI FFT 
    subgraph RRI_FS_PS_output
        data
        Total_power_dB
    end

    Frequency_response_and_Power_spectrum-.->RRI_FR_PS
    pkg-.->RRI_FR_PS
    RR_Class-.->RRI_FR_PS
    
    plot_graph_SV-->RRI_FR_PS-->RRI_FS_PS_output

%% SV FFT
    subgraph SV_FS_PS_output
        data
        Total_power_dB
    end
    
    Frequency_response_and_Power_spectrum-.->SV_FS_PS
    
    pkg-.->SV_FS_PS
    RRI_FR_PS-->SV_FS_PS-->SV_FS_PS_output

%% final calculate the HF/LF
    subgraph HF_LF_output
    CW
    HT
    end

    pkg-.->Pw_Sp_HF_LF
    RR_Class-.->Pw_Sp_HF_LF
    SV_FS_PS-->Pw_Sp_HF_LF-->HF_LF_output

```