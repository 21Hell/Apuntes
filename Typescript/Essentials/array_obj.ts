let hobbies = ['Reading', 'Gaming', 'Cooking'];


let user:(string | number)[];





let users: Array<(string | number)>;





let posibleResults:  [number,number];

posibleResults = [5, 10];









let user = {
    name: string,
    age: number,
    isActive: boolean,
    hobbies: string[],
    role: {
        title: string,
        level: number
    }
} = {
    name: "John Doe",
    age: 30,
    isActive: true,
    hobbies: ["Reading", "Gaming", "Cooking"],
    role: {
        title: "Admin",
        level: 1
    }
};









let val: {} = 'Value';




console.log(val);








let data: Record<string,number | string>;

data = {
    id: 1,
    name: "John Doe"
};
