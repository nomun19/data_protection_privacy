import pandas as pd


def calculate_qstar_block_counts(table, quasi_identifier, sensitive_attribute):
    qstar_block_counts = {}
    for _, row in table.iterrows():
        qstar = tuple(row[quasi_identifier])
        s_value = row[sensitive_attribute]

        if qstar not in qstar_block_counts:
            qstar_block_counts[qstar] = {s_value: 1}
        else:
            if s_value not in qstar_block_counts[qstar]:
                qstar_block_counts[qstar][s_value] = 1
            else:
                qstar_block_counts[qstar][s_value] += 1

    return qstar_block_counts


def check_l_diversity(qstar_block_counts, l):
    for s_counts in qstar_block_counts.values():
        if len(s_counts) < l:
            return False

    return True


def l_diversity(table, quasi_identifier, sensitive_attribute, l):
    qstar_block_counts = calculate_qstar_block_counts(table, quasi_identifier, sensitive_attribute)
    return check_l_diversity(qstar_block_counts, l)
def main():
    dataset_path = 'adult.csv'
    # read data
    data_original = pd.read_csv(dataset_path)
    # get columns
    data_columns = data_original.columns
    print(data_columns)


    quasi_identifiers = ['age', 'gender', 'race', 'marital-status']
    sensitive_attribute = 'income'

    # Set ℓ_value
    l_value = 3

    # Apply ℓ-Diversity
    df_anonymized = l_diversity(data_original, quasi_identifiers, sensitive_attribute, l_value)
    print(data_original.head())
    print(df_anonymized)

if __name__ == "__main__":
    main()