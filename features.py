import pandas as pd

def split_and_save_raw_data(ps2_path, fs1_path, profile_path, train_size=2000, save_dir='data/'):
    """
    Load raw data files, split into training and test sets by number of cycles,
    and save the split files separately.
    
    Arguments:
    - ps2_path: path to PS2.txt file
    - fs1_path: path to FS1.txt file
    - profile_path: path to profile.txt file
    - train_size: number of cycles to use for training (default 2000)
    - save_dir: directory where to save the split files (default 'data/')
    
    Returns:
    - None (saves files to disk)
    """
    
    # Load raw data
    ps2 = pd.read_csv(ps2_path, sep='\t', header=None)
    fs1 = pd.read_csv(fs1_path, sep='\t', header=None)
    profile = pd.read_csv(profile_path, sep='\t', header=None)

    # Check that number of cycles is consistent across files
    n = len(profile)
    assert len(ps2) == n and len(fs1) == n, "Number of cycles mismatch between files"

    # Split train/test
    ps2_train = ps2.iloc[:train_size]
    ps2_test = ps2.iloc[train_size:]

    fs1_train = fs1.iloc[:train_size]
    fs1_test = fs1.iloc[train_size:]

    profile_train = profile.iloc[:train_size]
    profile_test = profile.iloc[train_size:]

    # Save split files
    ps2_train.to_csv(f'{save_dir}/train/ps2_train.txt', sep='\t', header=False, index=False)
    ps2_test.to_csv(f'{save_dir}/test/ps2_test.txt', sep='\t', header=False, index=False)

    fs1_train.to_csv(f'{save_dir}/train/fs1_train.txt', sep='\t', header=False, index=False)
    fs1_test.to_csv(f'{save_dir}/test/fs1_test.txt', sep='\t', header=False, index=False)

    profile_train.to_csv(f'{save_dir}/train/profile_train.txt', sep='\t', header=False, index=False)
    profile_test.to_csv(f'{save_dir}/test/profile_test.txt', sep='\t', header=False, index=False)

    print(f"Train/test split done: {train_size} cycles train, {n - train_size} cycles test.")
    print(f"Files saved in {save_dir}")


