


Basic Types in TypeScript



string


number

boolean







# Array

let hobbies = ['Reading', 'Gaming', 'Cooking'];


let user:(string | number)[];


let users: Array<(string | number)>;


# Tuple

let posibleResults:  [number,number];

posibleResults = [5, 10];




# Complex Types

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


# {}

let val: {} = 'Value';


undefined and null are not allowed 





# Enum

Enum are a special "class" that represents a group of constants (unchangeable variables).

enum UserRole {
  User = 0,
  Admin = 1,
  Guest = 2
}
let userRole: UserRole = UserRole.User;


enum UserRole {
    User = 'User',
    Admin = 'Admin',
    Guest = 'Guest'
}

let userRole: UserRole = UserRole.User;




# Enum Literal Types


let userRole:'admin' | 'user' | 'guest' = 'admin';


userRole = 'user';




# Type Aliases

type UserRole = 'admin' | 'user' | 'guest';


function getUserRole(role: UserRole): string {
    return `User role is: ${role}`;
}  



# Return Types

function getUserRole(role: UserRole): string {
    return `User role is: ${role}`;
}

function add(a: number, b: number): number {
    return a + b;
}

function turnOnLight(): boolean {
    return true;
}
