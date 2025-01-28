# Parameters
learning_rate = 0.5
theta = 1  # This is the threshold (adjusted for the logic function)

# Logic gate training data for AND gate
and_training_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
and_labels = [0, 0, 0, 1]  # AND outputs

# Logic gate training data for OR gate
or_training_data = [
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
]
or_labels = [0, 1, 1, 1]  # OR outputs

# Initialize weights to zeros
w1, w2 = 0.0, 0.0  # Initial weights for two inputs

# Training for AND gate
print("Training AND Gate:")
for _ in range(10):  # Limit iterations for AND gate
    total_error = 0
    for i in range(len(and_training_data)):
        x1, x2 = and_training_data[i]
        target = and_labels[i]

        # Calculate weighted sum
        weighted_sum = w1 * x1 + w2 * x2
        
        # Predict output
        if weighted_sum >= theta:
            output = 1
        else:
            output = 0

        # Update weights if the output isn't the target
        if output != target:
            total_error += 1
            # Update weights
            w1 += learning_rate * (target - output) * x1
            w2 += learning_rate * (target - output) * x2
            
            print(f"Updated weights to w1: {w1}, w2: {w2}")  # Debugging statement

    print(f"Total errors for AND gate: {total_error}")
    if total_error == 0:
        break

# Test the perceptron for AND gate
print("AND Gate Predictions:")
for i in range(len(and_training_data)):
    x1, x2 = and_training_data[i]
    weighted_sum = w1 * x1 + w2 * x2
    if weighted_sum >= theta:
        output = 1
    else:
        output = 0
    print(f"Input: {and_training_data[i]}, Prediction: {output}")


# Reset weights for OR gate
w1, w2 = 0.0, 0.0  # Reinitialize weights

# Training for OR gate
print("\nTraining OR Gate:")
for _ in range(10):  # Limit iterations for OR gate
    total_error = 0
    for i in range(len(or_training_data)):
        x1, x2 = or_training_data[i]
        target = or_labels[i]

        # Calculate weighted sum
        weighted_sum = w1 * x1 + w2 * x2
        
        # Predict output
        if weighted_sum >= theta:
            output = 1
        else:
            output = 0

        # Update weights if the output isn't the target
        if output != target:
            total_error += 1
            # Update weights
            w1 += learning_rate * (target - output) * x1
            w2 += learning_rate * (target - output) * x2
            
            print(f"Updated weights to w1: {w1}, w2: {w2}")  # Debugging statement

    print(f"Total errors for OR gate: {total_error}")
    if total_error == 0:
        break

# Test the perceptron for OR gate
print("OR Gate Predictions:")
for i in range(len(or_training_data)):
    x1, x2 = or_training_data[i]
    weighted_sum = w1 * x1 + w2 * x2
    if weighted_sum >= theta:
        output = 1
    else:
        output = 0
    print(f"Input: {or_training_data[i]}, Prediction: {output}")
