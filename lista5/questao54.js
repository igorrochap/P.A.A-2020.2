function highestSumSequence(list){
    let sums = [], subsequency = []
    let sum = 0, currentSum = 0, lastElementSum = 0
    
    sums[0] = list[0]
    for(let i = 1; i < list.length; i++){
        sums.push(Math.max(list[i], sums[i - 1] + list[i]))
    }
    
    for(let i = 0; i < list.length; i++){
        if(sums[i] > sum){
            lastElementSum = i
            sum = sums[i]
        }
    }

    let currentIndex = lastElementSum

    while (sum != currentSum) {
        currentSum += list[currentIndex]
        currentIndex = currentIndex - 1
    }
    
    for(let i = currentIndex + 1; i < lastElementSum + 1; i++){
        subsequency.push(list[i])
    }
    
    console.log(`Subsequency: [${subsequency}]`)
    return sum
}

let list = [5, 15, -30, 10, -5, 40, 10]
console.log(highestSumSequence(list))