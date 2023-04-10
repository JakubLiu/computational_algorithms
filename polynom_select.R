# reading and cleaning the data___________________________________________________________________________________

library(data.table)

windmill <- fread("C:/Users/Lenovo/Desktop/STUDIA/BIOINFORMATYKA/SEMESTR_V/ALGORYTMY/sprawozdanie4/windmill.txt")

colnames(windmill) <- c("wind_velocity", "dc_power")

windmill <- windmill[3:nrow(windmill),]

plot(windmill$wind_velocity, windmill$dc_power, col = 'black', type = 'p', lwd = 5)

windmill$wind_velocity <- as.numeric(windmill$wind_velocity)

windmill$dc_power <- as.numeric(windmill$dc_power)

head(windmill)




mammals <- fread("C:/Users/Lenovo/Desktop/STUDIA/BIOINFORMATYKA/SEMESTR_V/ALGORYTMY/sprawozdanie4/mammals.txt")
mammals <- mammals[,4:5]
colnames(mammals) <- c("body_length", "relative_speed")
head(mammals)
mammals$body_length <- as.numeric(mammals$body_length)
mammals$relative_speed <- as.numeric(mammals$relative_speed)
plot(mammals$relative_speed, mammals$body_length, lwd = 5, col = 'black', type = 'p')



# function_____________________________________________________________________________________________________________________________________

# data ==> plik (musi być oczyszczony)
# pierwsza kolumna danych musi być zmienną objaśniającą, druga kolumna danych musi być zmienną objaśnianą
# min ==> minimaly stopień wielomianu
# max ==> maksymalny stopień wielomianu

polynom_select <- function(data, min = 1, max = 5){
  
  if(max <= nrow(data)){
  
    counter <- 3
    max <- max + 3
    colnames(data)[2] <- "response_variable"
    colnames(data)[1] <- "predictor_variable"
    plot(data$predictor_variable, data$response_variable, col = "blue", ylab = 'response variable', xlab = 'predictor variable', lwd = 5)
    title(main = "Data")
    Rsq_vec <- min-4:max-4
    model_vec <- min-4:max-4
    error_df_vec <- min-4:max-4
  
  
    for(i in min+1:max-1){
    
      if(counter <= max-1){
    
        data[, paste0("new_column", i)] <- data[,1]^i
        current_model <- paste("model", i, sep = "_")
        current_model <- lm(data$response_variable ~ ., data = data[, 3:counter])
        counter <- counter + 1
        current_model_summary <- summary(current_model)
        Rsq_vec[i] <- current_model_summary$r.squared
        model_vec[i] <- i
        error_df_vec[i] <- current_model_summary$sigma/current_model_summary$fstatistic[3]
      
      
        print(summary(current_model))
        print("-----------------------------------------------------------------------------------------------------------------------------")
          }
  }
    #print(paste0("Najlepsze dopasowanie osiągamy dla wielomianu stopnia: ",model_vec[which.max(Rsq_vec)]))
    plot(model_vec, Rsq_vec, col = "blue", lwd = 5, xlab = 'stopień wielomianu', ylab = 'R^2')
    title(main = "Zależność R^2 od stopnia wielomianu")
    
    print(paste0("Najlepsze dopasowanie osiągamy dla wielomianu stopnia: ",model_vec[which.min(error_df_vec)]))
    plot(model_vec, error_df_vec, col = "blue", lwd = 5, xlab = 'stopień wielomianu', ylab = 'błąd / stopnie swobody')
    title(main = "Zależność stosunku błędu do stopni swobody od stopnia wielomianu")
    error_df_vec
  }
  else{
    
    print("Stopień wielomianu nie może być wyższy niż liczba obserwacji.")
  }
}


# demonstration__________________________________________________________________________________________________________________________________

polynom_select(data = windmill, min = 1, max = 5)

polynom_select(data = mammals, min = 1, max = 5)
