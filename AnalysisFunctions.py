class Analyze:

    #Calculate and return average age
    def AverageAge(self, ages):
        total_sum, count, average_age = 0, 0, 0

        for age in ages:
            total_sum += age
            count += 1
        average_age = total_sum/count if count > 0 else 0 #prevent division by zero
        average_age = round(average_age, 2)
        return average_age

    #print average age
    def PrintAverageAge(self, ages):
        average_age = self.AverageAge(ages)
        print("The average age in this dataset is: " + str(average_age))

    #Calculate where the majority of the individuals are from
    def MostCommonRegion(self, region):
        region_count = {}
        total_count = 0
        for row in region:
            if row not in region_count:
                region_count[row] = 1 #initialize the region count to 1 if it's a new region added to the dictionary
            else:
                region_count[row] += 1 #increment count if the region was recorded in the dictionary

            total_count += 1
        #Grab max value from the dictionary
        max_key = max(region_count, key=region_count.get)

        #Print the region that has the max value in the dictionary (most common region)
        print("The most common region in this data set is the: " + str(max_key) + " region with a count of: " + str(region_count[max_key]) + " out of " + str(total_count) + ".")

    #Calculate the probability that an infividual with children are male or female
    def ProbabilityMaleOrFemale(self, sex, strChildren):        
        intChildren = [int(i) for i in strChildren] #Convert children values from string to int using list comprehension
        total_individuals_with_children = 0
        males_with_children = 0
        females_with_children = 0

        for sex, children in zip(sex, intChildren):
            if children > 0:
                total_individuals_with_children += 1 #increment total individuals with children
                if sex.upper() == "MALE":
                    males_with_children += 1 #increment male with children count

                elif sex.upper() == "FEMALE":
                    females_with_children += 1 #increment female with children count

        male_probability = males_with_children / total_individuals_with_children if total_individuals_with_children > 0 else 0
        female_probability = females_with_children / total_individuals_with_children if total_individuals_with_children > 0 else 0

        #Round probabilities
        male_probability = round(male_probability, 2)
        female_probability = round(female_probability, 2)

        results = {'Male Probability': male_probability, 'Female Probability': female_probability, 'Total Individuals With Children': total_individuals_with_children}

        print("\nDisplaying results of the probabilty than an individual with one or more children are male or female.\n")
        return results
                