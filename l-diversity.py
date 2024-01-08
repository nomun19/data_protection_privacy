import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def check_k_anonymity(table, quasi_identifiers, k):
    group_counts = table.groupby(quasi_identifiers).size()
    print(group_counts)
    return all(count >= k for count in group_counts)

def age_anonymization(table):
    anonymized_table = table.copy()
    anonymized_table['age'] = anonymized_table['age'].astype(str)
    for index, row in anonymized_table.iterrows():
        if int(row['age']) < 30:
            anonymized_table.at[index, 'age'] = '30>'
        else:
            age = int(int(row['age']) / 10)
            if age >= 7:
                age = 7
            anonymized_table.at[index, 'age'] = str(age) + '*'
    return anonymized_table

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

    quasi_identifiers = ['age', 'gender', 'native-country', 'marital-status']
    sensitive_attribute = 'income'

    # show the distribution of age
    sns.kdeplot(data_original['age'], fill=True)
    plt.title('Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Density')
    plt.show()

    # anonymize the age attribute
    anonymized_data = age_anonymization(data_original)
    # print(anonymized_data.head())


    # show the gender distribution of age
    df = data_original.dropna(subset=['age'])
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='age', hue='gender', multiple='stack', bins=20, kde=True)
    plt.title('Gender Distribution of Age')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.show()

    # anonymize the gender
    anonymized_data['gender'] = '*'

    # show corralation of age and race
    sns.countplot(x='age', hue='race', data=anonymized_data)
    plt.show()


    # anonymize the native country
    anonymized_data['native-country'] = '*'
    # anonymize the marital status
    anonymized_data['marital-status'] = '*'

    print(check_k_anonymity(anonymized_data, quasi_identifiers, 5))

    # show distribution of occupation by income
    cross_tab = pd.crosstab(data_original['occupation'], data_original['income'])

    # bar chart
    cross_tab.plot(kind='bar', stacked=True, color=['green', 'red'])
    plt.title('Occupation Distribution by Income')
    plt.xlabel('Occupation')
    plt.ylabel('Number of Individuals')
    plt.legend(title='Income', labels=['<=50K', '>50K'])
    plt.show()

    # Set ℓ_value
    l_value = 2

    # Apply ℓ-Diversity
    df_anonymized = l_diversity(anonymized_data, quasi_identifiers, sensitive_attribute, l_value)
    # print(data_original.head())
    print(df_anonymized)

if __name__ == "__main__":
    main()