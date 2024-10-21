package com.example.springbootmybatis.pojo;

import java.util.Date;

public class User {
    private Integer id;
    private String username;
    private String password;
    private String nickname;
    private String email;
    private String phone;
    private String gender;
    private String bank_id;
    private String card_id;
    private String address;
    private String wx_id;
    private String avatar;
    private Date create_time;


    public User(Integer id, String username, String password, String nickname, String email, String phone, String gender, String bank_id, String card_id, String address, String wx_id, String avatar, Date create_time) {
        this.id = id;
        this.username = username;
        this.password = password;
        this.nickname = nickname;
        this.email = email;
        this.phone = phone;
        this.gender = gender;
        this.bank_id = bank_id;
        this.card_id = card_id;
        this.address = address;
        this.avatar = avatar;
        this.wx_id = wx_id;
        this.create_time = create_time;
    }

    public Integer getId() { return id; }
    public void setId() { this.id = id; }
    public  String getUsername() { return username; }
    public void setUsername() { this.username = username; }
    public  String getPassword() { return password; }
    public void setPassword() { this.password = password; }

    public String getNickname() {
        return nickname;
    }

    public void setNickname(String nickname) {
        this.nickname = nickname;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }

    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }

    public String getBank_id() {
        return bank_id;
    }

    public void setBank_id(String bank_id) {
        this.bank_id = bank_id;
    }

    public String getCard_id() {
        return card_id;
    }

    public void setCard_id(String card_id) {
        this.card_id = card_id;
    }

    public String getWx_id() {
        return wx_id;
    }

    public void setWx_id(String wx_id) {
        this.wx_id = wx_id;
    }

    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }

    public String getAvatar() {
        return avatar;
    }

    public void setAvatar(String avatar) {
        this.avatar = avatar;
    }

    public Date getCreate_time() {
        return create_time;
    }

    public void setCreate_time(Date create_time) {
        this.create_time = create_time;
    }
}
